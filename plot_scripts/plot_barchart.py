import matplotlib.pyplot as plt
import numpy as np

# Create figure and first axis
# Set up LaTeX rendering
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "mathtext.fontset": "cm",
    "font.size": 24
})

plt.rcParams.update(plt.rcParamsDefault)






colors = ['forestgreen','crimson', "royalblue"]
colors = ['#6a5acd', '#20b2aa', '#ff7f50']  # Slate Blue, Light Sea Green, Coral
colors = ['#8e44ad', '#16a085', '#d35400']  # Purple, Teal, Orange
colors = ['#64b5f6', '#81c784', '#ba68c8']  # Sky Blue, Mint Green, Lavender Purple
colors = ['#9575cd', '#4db6ac', '#f06292']  # Medium Purple, Teal, Pink
colors = ['#80deea', '#9fa8da', '#ffcc80']  # Light Cyan, Periwinkle, Light Orange
colors = ['#64b5f6', '#9575cd', '#f06292']  # sky blue,Medium Purple, Pink

brat = (0.5411764705882353, 0.807843137254902, 0)
brat_pink = "#f55ebb"
find_colour = brat
bounce_colour = "#f06292"
baoding_colour = '#64b5f6'

category_colors = plt.cm.tab10(np.linspace(0, 1, 3))
find_colour = colors[0]
bounce_colour = colors[1]
baoding_colour = colors[2]

from plot import get_readers
import neurips_plots
from neurips_plots import ppo_colour, prop_colour, dynamics_colour, memory_colour, recon_colour

log_dir = "/home/elle/code/external/roto/paper_results"
output_dir = "/home/elle/code/external/roto/paper_results/plots"
import matplotlib.pyplot as plt
import numpy as np
import os

from tbparse import SummaryReader

plt.rcParams.update(plt.rcParamsDefault)
# plt.style.use('bmh')
plt.style.use('ggplot')  # Good for accessibility
# Set up LaTeX rendering
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "mathtext.fontset": "cm",
    "font.size": 24
})


plt.rcParams.update(plt.rcParamsDefault)

fig, ax = plt.subplots(figsize=(5, 4))
# fig, ax = plt.subplots(figsize=(6, 4))


from matplotlib import rcParams




# Set DPI
dpi = 600

plot_raw = False

def get_metrics(exp_dict):
    max_values = []
    mean_values = []

    experiment_names = exp_dict["run_names"]



    for i, experiment_name in enumerate(experiment_names):

        parent_experiment_dir = os.path.join(log_dir, exp_dict["log_dir"], exp_dict["experiment_name"])


        print(i, experiment_name)

        readers = get_readers(parent_experiment_dir, experiment_name)

        # min_length=100
        mean_rewards = []
        step = []

        # loop through seeds
        for reader in readers:
            df = reader.scalars

            tag = exp_dict["tag"]
            # tags = exp_dict["tags"]

            metric = df[df["tag"] == tag]
            
            step = metric["step"].to_numpy() / 1e6
            metric = metric["value"].to_numpy()
            
            if tag == "num_rotations":
                run_rewards = metric /2
            elif tag == "timesteps_to_find_object_easy" or tag == "timesteps_to_find_object_med" or tag == "timesteps_to_find_object_hard":
                # 1 timestep = 1/60 seconds
                run_rewards = metric / 60
            elif tag == "bounce_reward":
                run_rewards = metric / 10
            else:
                run_rewards = metric

            mean_rewards.append(run_rewards)
            if plot_raw:
                plt.plot(step, run_rewards, label=exp_dict["legend_names"][i])

        
        if "bar_chart" in exp_dict.keys():
            mean_rewards = np.array(mean_rewards)
            max_value = np.max(mean_rewards)
            print(np.shape(mean_rewards))

            if tag == "timesteps_to_find_object_easy" or tag == "timesteps_to_find_object_med" or tag == "timesteps_to_find_object_hard":
                
                # weird timestep in beginning
                mean_rewards = mean_rewards[:, 5:]

                # subtract to get time remaining
                mean_rewards = mean_rewards

                mean = np.mean(mean_rewards, axis=0)
                min_mean = np.min(mean)
                min_value = np.min(mean_rewards)

                min_mean = 5- min_mean
                min_value = 5-min_value

                print("min_mean", min_mean)
                print("min", min_value)

                mean_values.append(min_mean)
                max_values.append(min_value)
            else:
                mean = np.mean(mean_rewards, axis=0)
                max_mean = np.max(mean)
                mean_values.append(max_mean)
                max_values.append(max_value)
            continue

    return mean_values, max_values

def main():
    fig, axes = plt.subplots(1, 3, figsize=(9, 2.5))
    ax1, ax2, ax3 = axes

    franka_exp = neurips_plots.franka_barchart
    bounce_exp = neurips_plots.bounce_ssl_rotations_barchart
    baoding_exp = neurips_plots.baoding_ssl_rotations_barchart

    franka_mean_values, franka_max_values = get_metrics(franka_exp)
    bounce_mean_values, bounce_max_values = get_metrics(bounce_exp)
    baoding_mean_values, baoding_max_values = get_metrics(baoding_exp)

    print("*****************************")
    print(franka_mean_values)
    print(bounce_mean_values)
    print(baoding_mean_values)
    print("*****************************")
    print(franka_max_values)
    print(bounce_max_values)
    print(baoding_max_values)

    fontsize=8

    width=0.7

    x_labels = ["p","pt", "+FR", "+TR", "+FD", "+TFD", "+FD+$N_{rollouts}$"]
    legend_labels = [r"PPO($o^{prop}$)", r"PPO($o^{prop}, o^{tact}$)", "+FR", "+TR", "+FD", "+TFD", r"+FD+$N_{rollouts}$"]

    colours = [prop_colour, ppo_colour, recon_colour, recon_colour, dynamics_colour, dynamics_colour, memory_colour]

    styles = [
        {'facecolor': prop_colour, 'edgecolor': prop_colour, 'linestyle': '-', 'linewidth': 2},
        {'facecolor': ppo_colour, 'edgecolor': ppo_colour, 'linestyle': '-', 'linewidth': 2},
        {'facecolor': recon_colour, 'edgecolor': recon_colour, 'linestyle': '-', 'linewidth': 2},
        {'facecolor': recon_colour, 'edgecolor': recon_colour, 'linestyle': '--', 'linewidth': 3},
        {'facecolor': dynamics_colour, 'edgecolor': dynamics_colour, 'linestyle': '-', 'linewidth': 2},
        {'facecolor': dynamics_colour, 'edgecolor': dynamics_colour, 'linestyle': '--', 'linewidth': 3},
        {'facecolor': memory_colour, 'edgecolor': memory_colour, 'linestyle': '-', 'linewidth': 2},]

    ax1.grid(True, alpha=0.3, zorder=0)
    ax2.grid(True, alpha=0.3, zorder=0)
    ax3.grid(True, alpha=0.3, zorder=0)

    # Data for multiple tasks
    x = np.arange(7)

    # First task on primary axis
    alphas = [0.7, 0.25]
    # ax1.bar(x, franka_mean_values, width=width, color=colours, alpha=main_alpha)
    # ax1.bar(x, franka_max_values, width=width, color=colours, alpha=0.25)
    
    for j, values in enumerate([franka_mean_values, franka_max_values]):
        for i, (label, value) in enumerate(zip(x, values)):
            ax1.bar(
                label,
                value,
                color=styles[i]['facecolor'],
                edgecolor=styles[i]['edgecolor'],
                linestyle=styles[i]['linestyle'],
                linewidth=styles[i]['linewidth'],
                width=0.7,
                alpha=alphas[j]
            )

    for j, values in enumerate([bounce_mean_values, bounce_max_values]):
        for i, (label, value) in enumerate(zip(x, values)):
            ax2.bar(
                label,
                value,
                color=styles[i]['facecolor'],
                edgecolor=styles[i]['edgecolor'],
                linestyle=styles[i]['linestyle'],
                linewidth=styles[i]['linewidth'],
                width=0.7,
                alpha=alphas[j]
            )

    for j, values in enumerate([baoding_mean_values, baoding_max_values]):
        for i, (label, value) in enumerate(zip(x, values)):
            if j == 0:
                ax3.bar(
                    label,
                    value,
                    color=styles[i]['facecolor'],
                    edgecolor=styles[i]['edgecolor'],
                    linestyle=styles[i]['linestyle'],
                    linewidth=styles[i]['linewidth'],
                    width=0.7,
                    alpha=alphas[j],
                    label=legend_labels[i]
                )
            else:
                ax3.bar(
                    label,
                    value,
                    color=styles[i]['facecolor'],
                    edgecolor=styles[i]['edgecolor'],
                    linestyle=styles[i]['linestyle'],
                    linewidth=styles[i]['linewidth'],
                    width=0.7,
                    alpha=alphas[j],
                )

    label_size = 12
    ax1.set_title('Remaining time after found (s)', fontsize=fontsize)
    ax1.tick_params(axis='y', labelsize=fontsize)
    ax1.set_ylim(franka_exp["y_min"], franka_exp["y_max"])
    ax1.set_xticks([])
    ax1.set_xticklabels([])

    # Second task on first twin axis (right side)
    # ax2 = ax1.twinx()
    # ax2.spines['right'].set_position(('outward', 0))  # Default right position
    ax2.set_title('Number of bounces', fontsize=fontsize)
    ax2.tick_params(axis='y', labelsize=fontsize)
    ax2.set_ylim(bounce_exp["y_min"], bounce_exp["y_max"])

    # Third task on second twin axis (further right)
    # ax3 = ax1.twinx()
    # ax3.spines['right'].set_position(('outward', 60))  # Moved 60 points right
    ax3.set_title('Number of Baoding rotations', fontsize=fontsize)
    ax3.tick_params(axis='y', labelsize=fontsize)
    ax3.set_ylim(baoding_exp["y_min"], baoding_exp["y_max"])
    # Common x-axis settings
    # plt.xticks(x, ["PPO(p)","PPO(pt)", "+recon", "+tac_recon", "+dyn", "+dyn+mem"])

    plt.tight_layout()

    ax2.set_xticks([])
    ax2.set_xticklabels([])
    ax3.set_xticks([])
    ax3.set_xticklabels([])

    # ax1.set_xticks(x, x_labels)
    # ax2.set_xticks(x, x_labels)
    # ax3.set_xticks(x, x_labels)
    # ax1.tick_params(axis='both', labelsize=fontsize)
    # ax2.tick_params(axis='both', labelsize=fontsize)
    # ax3.tick_params(axis='both', labelsize=fontsize)


    # Add legend to the right of the third subplot
    ax3.legend(loc='center left', bbox_to_anchor=(1.05, 0.5), fontsize=fontsize)

    # Adjust layout to make room for the legend
    fig.subplots_adjust(right=0.8)  # Adjust this value as needed to fit the legend

    plt.tight_layout()
    # plt.show()

    plt.savefig("paper_results/plots/bar_chart.pdf", dpi=100, bbox_inches='tight', pad_inches=0.05)



if __name__ == "__main__":

    main()