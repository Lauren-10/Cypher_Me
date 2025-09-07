#The Crown Jewel of the Repo


function isInUpperTriangle(P::Tuple{Int64,Int64},T::Tuple{Int64,Int64,Int64})
    return P[1] ≥ T[1] && P[2] ≤ T[2] && P[2]-P[1] ≥ T[3]
end

function isInLowerTriangle(P::Tuple{Int64,Int64},T::Tuple{Int64,Int64,Int64})
    return P[1] ≤ T[1] && P[2] ≥ T[2] && P[2]-P[1] ≤ T[3]
end

function rectSize(Q::Tuple{Int64,Int64,Int64,Int64})
    return max(Q[2]-Q[1]+1,0)*max(Q[4]-Q[3]+1,0)
end

function upperTriaSize(T::Tuple{Int64,Int64,Int64})
    t = max(T[2]-T[1]-T[3]+1,)
    return t*(t+1)÷2
end

function lowerTriaSize(T::Tuple{Int64,Int64,Int64})
    t = max(T[3]-(T[2]-T[1])+1,0)
    return t*(t+1)÷2
end

getRect(R::Vector{Int64}) = (R[1]+R[3],R[2]+R[4],R[5]+R[3],R[6]+R[4])
getUpperTriangle(R::Vector{Int64},Q::Tuple{Int64,Int64,Int64,Int64}) = (Q[1],Q[4],Q[4]-Q[1]-(R[4]-R[3])+1)
getLowerTriangle(R::Vector{Int64},Q::Tuple{Int64,Int64,Int64,Int64}) = (Q[2],Q[3],Q[3]-Q[2]+(R[4]-R[3])-1)

function g(N::Int64)
    R1 = [0,1,0,0,0,0]
    R2 = [0,0,0,1,0,0]
    R3 = [0,0,0,0,0,1]
    for n ∈ 2:N
        newR1 = [R2[1]-R3[2],R2[2]-R3[1],R2[3]-R3[4],R2[4]-R3[3],R2[5]-R3[6],R2[6]-R3[5]]
        newR3 = [R2[1]-R1[2],R2[2]-R1[1],R2[3]-R1[4],R2[4]-R1[3],R2[5]-R1[6],R2[6]-R1[5]]
        newR2 = R1.+R3
        R1 = newR1
        R2 = newR2
        R3 = newR3
    end
    Q1 = getRect(R1)
    T1U = getUpperTriangle(R1,Q1)
    T1L = getLowerTriangle(R1,Q1)
    Q2 = getRect(R2)
    T2U = getUpperTriangle(R2,Q2)
    T2L = getLowerTriangle(R2,Q2)
    Q3 = getRect(R3)
    T3U = getUpperTriangle(R3,Q3)
    T3L = getLowerTriangle(R3,Q3)
    C = 3*(rectSize(Q1)-upperTriaSize(T1U)-lowerTriaSize(T1L))^2
    D = 0
    for px ∈ Q2[1]:Q2[2],
        py ∈ Q2[3]:Q2[4]

        if isInUpperTriangle((px,py),T2U) || isInLowerTriangle((px,py),T2L)
            continue
        end
        tQ = (max(px-Q1[2],Q3[1]),min(px-Q1[1],Q3[2]),max(py-Q1[4],Q3[3]),min(py-Q1[3],Q3[4]))
        C -= 2*rectSize(tQ)
        tTL = (px-T1U[1],py-T1U[2],-T1U[3]+py-px)
        ItTL = (min(tTL[1],T3L[1]),max(tTL[2],T3L[2]),min(tTL[3],T3L[3]))
        C -= 4*lowerTriaSize(ItTL)
        ItTL = (min(tTL[1],Q3[2]),max(tTL[2],Q3[3]),tTL[3])
        C += 8*lowerTriaSize(ItTL)
        ItTL = (min(tTL[1],Q3[1]-1),max(tTL[2],Q3[4]+1),tTL[3])
        C += 8*lowerTriaSize(ItTL)
        ItTL = (min(tTL[1],Q3[1]-1),max(tTL[2],Q3[3]),tTL[3])
        C -= 8*lowerTriaSize(ItTL)
        ItTL = (min(tTL[1],Q3[2]),max(tTL[2],Q3[4]+1),tTL[3])
        C -= 8*lowerTriaSize(ItTL)
    end
    return C
end

function main()
    return g(16)
end

main()