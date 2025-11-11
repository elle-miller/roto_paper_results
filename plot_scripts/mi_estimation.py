import numpy as np
from sklearn.preprocessing import scale
from sklearn.neighbors import NearestNeighbors, KDTree
from scipy.special import digamma
from sklearn.decomposition import PCA
import pandas as pd
def compute_mi_cc(x, y, n_neighbors=3, metric="euclidean"):
    """Compute the mutual information between two continuous variables"""

    if not isinstance(x, np.ndarray):
        x = np.array(x)
    if not isinstance(y, np.ndarray):
        y = np.array(y)

    n_samples, _ = x.shape

    # make data have unit variance
    x = scale(x, with_mean=False, copy=True)
    y = scale(y, with_mean=False, copy=True)

    # Add small noise to continuous features as advised in Kraskov et. al.
    means = np.maximum(1, np.mean(np.abs(x), axis=0))
    x += (
        1e-10
        * means
        * np.random.randn(*x.shape)
    )
    means = np.maximum(1, np.mean(np.abs(y), axis=0))
    y += (
        1e-10
        * means
        * np.random.randn(*y.shape)
    )
    xy = np.hstack((x, y))

    # Here we rely on NearestNeighbors to select the fastest algorithm.
    nn = NearestNeighbors(metric=metric, n_neighbors=n_neighbors)

    nn.fit(xy)
    radius = nn.kneighbors()[0]
    radius = np.nextafter(radius[:, -1], 0)

    # KDTree is explicitly fit to allow for the querying of number of
    # neighbors within a specified radius
    kd = KDTree(x, metric=metric)
    nx = kd.query_radius(x, radius, count_only=True, return_distance=False)
    nx = np.array(nx) - 1.0

    kd = KDTree(y, metric=metric)
    ny = kd.query_radius(y, radius, count_only=True, return_distance=False)
    ny = np.array(ny) - 1.0

    mi = (
        digamma(n_samples)
        + digamma(n_neighbors)
        - np.mean(digamma(nx + 1))
        - np.mean(digamma(ny + 1))
    )

    return max(0, mi)

# NOTE: You need to ensure the compute_mi_cc function is defined in your environment
# and all imports (like scale, digamma, NearestNeighbors, KDTree) are available.
def compute_marginal_mi(z, s, n_neighbors=4):
    # --- Marginal MI Calculation ---
    marginal_mi_results = {}
    n_features_s = s.shape[1]

    for j in range(n_features_s):
        # Select the j-th column of S
        S_j = s[:, j]
        
        # Reshape S_j to (N, 1) as required by compute_mi_cc
        S_j_reshaped = S_j.reshape(-1, 1)
        
        # Calculate MI(Z_reduced; S_j)
        mi_value = compute_mi_cc(
            x=z,
            y=S_j_reshaped,
            n_neighbors=n_neighbors,
            metric="euclidean"
        )
        
        # Store the result
        marginal_mi_results[f"S_{j}"] = mi_value

    # --- Results ---
    # Convert to a Pandas Series for easy sorting and display
    mi_series = pd.Series(marginal_mi_results)

    print("\nMarginal Mutual Information Results (nats):")
    print(mi_series.sort_values(ascending=False))

    # Optional: Print the total of the marginal MIs
    # Note: The sum of marginal MIs is NOT equal to the total MI (MI(Z;S))
    print(f"\nSum of Marginal MIs: {mi_series.sum():.4f} nats")
def get_mis(files, z_reduced_dim, n_neighbors):
    mis = []
    for file in files:

        print(file)

        # 256-dim latent variable Z
        z = np.load(file)["z"]
        pca = PCA(n_components=z_reduced_dim)
        z = pca.fit_transform(z) 
        s = np.load(file)["s"]

        metric = "euclidean"
        # s_dim = [2,9,13]
        # s = s[:, s_dim]
        mi_correlated = compute_mi_cc(z, s, n_neighbors=n_neighbors, metric=metric)
        mis.append(mi_correlated)
        print(f"MI (Correlated): {mi_correlated:.4f}")

        compute_marginal_mi(z, s, n_neighbors=n_neighbors)

    return mis

if __name__ == "__main__":
    # 1. Setup Data
    np.random.seed(42)
    N = 5000  # Number of samples

    z_dim = 256
    z_reduced_dim = 9
    n_neighbors = 4

    bdm = "latents/baoding_dynamics.npz"
    brl = "latents/baoding_rl_only_pt.npz"
    btd = "latents/baoding_tactile_dynamics.npz"
    btr = "latents/baoding_tactile_recon.npz"
    bd = "latents/baoding_dynamics_only.npz"
    bfr = "latents/baoding_full_recon.npz"

    bod = "latents/bounce_dynamics.npz"
    borl = "latents/bounce_rl_only_pt.npz"
    botd = "latents/bounce_tactile_dynamics.npz"
    botr = "latents/bounce_tactile_recon.npz"

    bod = "latents/bounce_dynamics.npz"
    borl = "latents/bounce_rl_only_pt.npz"
    botd = "latents/bounce_tactile_dynamics.npz"
    botr = "latents/bounce_tactile_recon.npz"
    bofr = "latents/bounce_full_recon.npz"

    legend_labels = ["RL", "TR", "FD", "TD"]
    legend_labels = [r"PPO($o^{prop}, o^{tact}$)", "+FR", "+TR", "+FD", "+TFD", r"+FD+$N_{rollouts}$"]


    baoding_files = [brl, bfr, btr, bd, btd, bdm]
    bounce_files = [borl,  bofr, botr, bod, botd]
    baoding_mis = get_mis(baoding_files, z_reduced_dim, n_neighbors)
    bounce_mis = get_mis(bounce_files, z_reduced_dim, n_neighbors)


   
    x = np.arange(5)

    colors = ['#64b5f6', '#9575cd', '#f06292']  # sky blue,Medium Purple, Pink

    ppo_colour=colors[0]
    prop_colour = "orange"
    prop_no_action_colour = "#DA70D6"
    recon_colour="red" #colors[1]
    dynamics_colour="tab:green" #colors[2]
    memory_colour="purple" 

    
    styles = [
        # {'facecolor': prop_colour, 'edgecolor': prop_colour, 'linestyle': '-', 'linewidth': 2},
        {'facecolor': ppo_colour, 'edgecolor': ppo_colour, 'linestyle': '-', 'linewidth': 2},
        {'facecolor': recon_colour, 'edgecolor': recon_colour, 'linestyle': '-', 'linewidth': 2},
        {'facecolor': recon_colour, 'edgecolor': recon_colour, 'linestyle': '--', 'linewidth': 3},
        {'facecolor': dynamics_colour, 'edgecolor': dynamics_colour, 'linestyle': '-', 'linewidth': 2},
        {'facecolor': dynamics_colour, 'edgecolor': dynamics_colour, 'linestyle': '--', 'linewidth': 3},
        {'facecolor': memory_colour, 'edgecolor': memory_colour, 'linestyle': '-', 'linewidth': 2},]
    # ax1.bar(x, franka_mean_values, width=width, color=colours, alpha=main_alpha)
    # ax1.bar(x, franka_max_values, width=width, color=colours, alpha=0.25)
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 2, figsize=(8, 2))
    ax1, ax2 = axes
    
    for i, (label, value) in enumerate(zip(x, bounce_mis)):
        ax1.bar(
            label,
            value,
            color=styles[i]['facecolor'],
            edgecolor=styles[i]['edgecolor'],
            linestyle=styles[i]['linestyle'],
            linewidth=styles[i]['linewidth'],
            width=0.7,
            alpha=0.8
        )

    for i, (label, value) in enumerate(zip(x, baoding_mis)):
        ax2.bar(
            label,
            value,
            color=styles[i]['facecolor'],
            edgecolor=styles[i]['edgecolor'],
            linestyle=styles[i]['linestyle'],
            linewidth=styles[i]['linewidth'],
            width=0.7,
            label=legend_labels[i],
            alpha=0.8
        )

    # for i, (label, value) in enumerate(zip(x, bounce2_mis)):
    #     ax3.bar(
    #         label,
    #         value,
    #         color=styles[i]['facecolor'],
    #         edgecolor=styles[i]['edgecolor'],
    #         linestyle=styles[i]['linestyle'],
    #         linewidth=styles[i]['linewidth'],
    #         width=0.7,

    #     )

    ax1.grid(True, alpha=0.3, zorder=0)
    ax2.grid(True, alpha=0.3, zorder=0)

    ax1.set_title("Bounce", fontsize=10)
    ax2.set_title("Baoding", fontsize=10)

    ax1.set_ylim(0, max(bounce_mis)*1.1)
    ax2.set_ylim(0, max(baoding_mis)*1.1)
    ax1.set_xticks([])
    ax1.set_ylabel(r"$I(z_t;s_t)$ (nats)")
    ax1.set_xticks([])
    ax1.set_xticklabels([])
    ax2.set_xticks([])
    ax2.set_xticklabels([])


    fontsize=8
    ax1.tick_params(axis='y', labelsize=fontsize)
    ax2.tick_params(axis='y', labelsize=fontsize)
    # ax3.tick_params(axis='y', labelsize=fontsize)   

    # Add legend to the right of the third subplot
    ax2.legend(loc='center left', bbox_to_anchor=(1.05, 0.5), fontsize=8)
    # ax.set_title("Mutual Information between Z and S")
    # ax1.set_ylim(0.0, max(mis)*1.1)

    # Adjust layout to make room for the legend
    # fig.subplots_adjust(right=0.8)  # Adjust this value as needed to fit the legend

    plt.tight_layout()
    # plt.show()

    plt.savefig("paper_results/plots/mi.pdf", dpi=100, bbox_inches='tight', pad_inches=0.05)


    plt.show()