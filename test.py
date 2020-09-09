from blueqat import Circuit
from blueqat import vqe
from blueqat.pauli import qubo_bit as q

# 2量子ビットの量子もつれの回路です
Circuit().h[0].cx[0, 1].m[:].run(shots=100)

# 量子古典ハイブリッド計算に対応した、行列の固有値を求める回路です
hamiltonian = -3*q(0)-3*q(1)+2*q(0)*q(1)
result = vqe.Vqe(vqe.QaoaAnsatz(hamiltonian, step=2)).run()
print(result.most_common(12))
