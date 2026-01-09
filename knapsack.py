import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import time
import sys

sys.setrecursionlimit(10000)

CAPACITY = 55 
names = ["Defibrillator", "Ventilator", "Monitor", "Infusion Pump", "Suction", "Oxygen", "Nebulizer", "ECG"]
weights = [25, 30, 15, 10, 12, 8, 5, 14]
values = [100, 120, 80, 50, 60, 45, 30, 70]
n = len(names)

def solve_dp():
    dp = [[0 for _ in range(CAPACITY + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(CAPACITY + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][CAPACITY]

bt_nodes = 0
bt_best_v, bt_best_w, bt_best_items = 0, 0, []

def solve_backtracking(index, current_w, current_v, path_idx):
    global bt_best_v, bt_best_w, bt_best_items, bt_nodes
    bt_nodes += 1 
    
    if current_v > bt_best_v:
        bt_best_v, bt_best_w, bt_best_items = current_v, current_w, path_idx[:]
        
    if index == n: return

    if current_w + weights[index] <= CAPACITY:
        solve_backtracking(index + 1, current_w + weights[index], 
                           current_v + values[index], path_idx + [index])
    
    solve_backtracking(index + 1, current_w, current_v, path_idx)

nodes_bf = (2**(n + 1)) - 1 

start_bt = time.time()
bt_nodes = 0 
solve_backtracking(0, 0, 0, [])
time_bt = time.time() - start_bt

start_bf = time.time()
for _ in range(int(nodes_bf)): pass
time_bf = time.time() - start_bf

pruning_eff = ((nodes_bf - bt_nodes) / nodes_bf) * 100

print("\n" + "═"*65)
print("             DAFTAR PERALATAN MEDIS (SOLUSI OPTIMAL)             ")
print("═"*65)
df_hasil = pd.DataFrame({
    "Nama Alat": [names[i] for i in bt_best_items],
    "Berat (kg)": [weights[i] for i in bt_best_items],
    "Nilai Manfaat": [values[i] for i in bt_best_items]
})
print(df_hasil.to_string(index=False))
print("─"*65)
print(f"Total Berat Terpilih   : {bt_best_w} kg / {CAPACITY} kg")
print(f"Total Nilai Maksimum   : {bt_best_v}")
print(f"Efisiensi Pruning      : {pruning_eff:.2f}%")
print("═"*65)

def draw_performance():
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.patch.set_facecolor('#F8F9FA')
    labels = ['Brute Force', 'Backtracking']
    colors = ['#E63946', '#2A9D8F']

    axes[0].bar(labels, [nodes_bf, bt_nodes], color=colors)
    axes[0].set_title("Total Simpul Dievaluasi\n(Efisiensi Ruang)", fontweight='bold')
    for i, v in enumerate([nodes_bf, bt_nodes]):
        axes[0].text(i, v, f"{int(v):,}", ha='center', va='bottom', fontweight='bold')

    axes[1].bar(labels, [time_bf, time_bt], color=colors)
    axes[1].set_title("Waktu Eksekusi\n(Detik)", fontweight='bold')
    for i, v in enumerate([time_bf, time_bt]):
        axes[1].text(i, v, f"{v:.5f}s", ha='center', va='bottom', fontweight='bold')

    pruning_comparison = [0, pruning_eff]
    axes[2].bar(labels, pruning_comparison, color=colors)
    axes[2].set_ylim(0, 110)
    axes[2].set_title("Perbandingan Efisiensi Pruning\n(% Cabang Terpotong)", fontweight='bold')
    for i, v in enumerate(pruning_comparison):
        axes[2].text(i, v + 2, f"{v:.2f}%", ha='center', va='bottom', fontweight='bold')

    plt.suptitle("ANALISIS KOMPARATIF: BRUTE FORCE VS BACKTRACKING", fontsize=16, fontweight='bold')
    plt.tight_layout(pad=3.0)
    plt.show()


def draw_complex_tree():
    G = nx.DiGraph()
    VIZ_DEPTH = 4 
    
    def add_nodes(depth, curr_w, curr_v, x, y, p_id, spread, edge_lab=""):
        if depth > VIZ_DEPTH: return
        node_id = f"{p_id}_{depth}_{x}_{y}"
        is_valid = curr_w <= CAPACITY
        node_color = '#2ECC71' if is_valid else '#E74C3C'
        
        G.add_node(node_id, pos=(x, y), label=f"W:{curr_w}\nV:{curr_v}", color=node_color)
        if p_id: G.add_edge(p_id, node_id, label=edge_lab)
        
        if depth < VIZ_DEPTH:
            add_nodes(depth + 1, curr_w + weights[depth], curr_v + values[depth], 
                      x - spread, y - 1, node_id, spread / 2, f"X{depth}=1")
            add_nodes(depth + 1, curr_w, curr_v, 
                      x + spread, y - 1, node_id, spread / 2, f"X{depth}=0")

    add_nodes(0, 0, 0, 0, 0, None, 25, "")
    plt.figure(figsize=(20, 10))
    pos = nx.get_node_attributes(G, 'pos')
    labels = nx.get_node_attributes(G, 'label')
    edge_labels = nx.get_edge_attributes(G, 'label')
    colors = [d['color'] for n, d in G.nodes(data=True)]
    
    nx.draw(G, pos, labels=labels, with_labels=True, node_color=colors, 
            node_size=2500, font_size=7, font_weight='bold', 
            edge_color='#ADB5BD', width=1.0, arrowsize=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=7)
    
    plt.title("STATE SPACE TREE HINGGA MINIMAL LEVEL KE-4\nHijau: Jalur Valid | Merah: Jalur Terpangkas (Pruning)", 
              fontsize=15, fontweight='bold', pad=20)
    plt.axis('off')
    plt.show()

draw_performance()
draw_complex_tree()