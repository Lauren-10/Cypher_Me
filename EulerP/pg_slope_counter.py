#!/usr/bin/env python3
from fractions import Fraction
import json, time
from typing import Tuple, Dict, Any, Optional

Point = Tuple[Fraction, Fraction]
INF = ("INF",)

def parse_fraction(x) -> Fraction:
    if isinstance(x, int): return Fraction(x)
    if isinstance(x, str): return Fraction(x)
    raise TypeError(f"Unsupported number type: {type(x)}")

def parse_point(obj) -> Point:
    return (parse_fraction(obj[0]), parse_fraction(obj[1]))

def line_coeffs_through(p: Point, q: Point):
    (x1,y1),(x2,y2)=p,q
    A=y1-y2; B=x2-x1; C=x1*y2-x2*y1
    return (A,B,C)

def intersect_frac(L1,L2)->Optional[Point]:
    A1,B1,C1=L1; A2,B2,C2=L2
    det=A1*B2-A2*B1
    if det==0: return None
    x=(B1*C2-B2*C1)/det
    y=(C1*A2-C2*A1)/det
    return (x,y)

def slope_from_red(red_idx:int,P:Point):
    x,y=P
    if red_idx==0:
        if x==0: return INF
        return Fraction(y,x)
    elif red_idx==1:
        if x==1: return INF
        return Fraction(y,x-1)
    else:
        if x==0: return INF
        return Fraction(y-1,x)

def triple_from_pair(j:int,r:int,a,b):
    if a==INF or b==INF: return None
    if j==0 and r==1:
        s1,s2=a,b
        if s2==0: return None
        s3=s1+Fraction(s1,s2)-1
        return (s1,s2,s3)
    if j==0 and r==2:
        s1,s3=a,b; denom=1-s1+s3
        if denom==0: return None
        s2=Fraction(s1,denom); return (s1,s2,s3)
    if j==1 and r==0:
        s2,s1=a,b
        if s2==0: return None
        s3=s1+Fraction(s1,s2)-1
        return (s1,s2,s3)
    if j==1 and r==2:
        s2,s3=a,b; denom=s2+1
        if denom==0: return None
        s1=Fraction(s2*(s3+1),denom)
        return (s1,s2,s3)
    if j==2 and r==0:
        s3,s1=a,b; denom=1-s1+s3
        if denom==0: return None
        s2=Fraction(s1,denom); return (s1,s2,s3)
    if j==2 and r==1:
        s3,s2=a,b; denom=s2+1
        if denom==0: return None
        s1=Fraction(s2*(s3+1),denom)
        return (s1,s2,s3)
    return None

def count_nextday_points_threshold(cert:Dict[str,Any],day_index:int,cap:int=24000):
    reds=[parse_point(p) for p in cert["reds"]]
    B=[parse_point(p) for p in cert["blues0"]]
    N_points=[]
    for d in range(day_index):
        day=cert["days"][d]
        Bset=set(B); today_new=[]
        for ent in day["entries"]:
            i,k,u_id,v_id,match=ent["i"],ent["k"],ent["u"],ent["v"],ent.get("match",0)
            j=3-i-k; Ri,Rk=reds[i],reds[k]
            u,v=B[u_id],B[v_id]
            if match==0: P=intersect_frac(line_coeffs_through(Ri,u),line_coeffs_through(Rk,v))
            else: P=intersect_frac(line_coeffs_through(Ri,v),line_coeffs_through(Rk,u))
            if P and P not in Bset and P not in reds:
                today_new.append((P,j)); B.append(P); Bset.add(P)
        if d==day_index-1: N_points=today_new
    S=[set() for _ in range(3)]
    for X in B:
        for r in range(3): S[r].add(slope_from_red(r,X))
    K=[[set() for _ in range(3)] for __ in range(3)]
    for X in B:
        s0=slope_from_red(0,X);s1=slope_from_red(1,X);s2=slope_from_red(2,X)
        K[0][1].add((s0,s1));K[1][0].add((s1,s0))
        K[0][2].add((s0,s2));K[2][0].add((s2,s0))
        K[1][2].add((s1,s2));K[2][1].add((s2,s1))
    U=[set() for _ in range(3)]
    for P,j in N_points: U[j].add(slope_from_red(j,P))
    seen=set();count=0
    for j in range(3):
        for r in range(3):
            if r==j: continue
            for a in U[j]:
                for b in S[r]:
                    if (a,b) in K[j][r]: continue
                    triple=triple_from_pair(j,r,a,b)
                    if not triple or triple in seen: continue
                    seen.add(triple); count+=1
                    if count>cap: return count,True
    return count,False

if __name__=="__main__":
    cert_file=input("Enter path to certificate JSON file: ").strip()
    t=int(input("Enter day index t (compute t→t+1): ").strip())
    cap=int(input("Enter cap (default 24000): ").strip() or "24000")
    with open(cert_file) as f:
        cert=json.load(f)
    t0=time.time()
    count,exceeded=count_nextday_points_threshold(cert,t,cap)
    print(f"t={t}: new_points={count} exceeded_cap={exceeded} cap={cap} time_sec={time.time()-t0:.3f}")
