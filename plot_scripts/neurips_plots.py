colors = ['forestgreen','crimson', "royalblue"]
colors = ['#6a5acd', '#20b2aa', '#ff7f50']  # Slate Blue, Light Sea Green, Coral
colors = ['#8e44ad', '#16a085', '#d35400']  # Purple, Teal, Orange
colors = ['#64b5f6', '#81c784', '#ba68c8']  # Sky Blue, Mint Green, Lavender Purple
colors = ['#9575cd', '#4db6ac', '#f06292']  # Medium Purple, Teal, Pink
colors = ['#80deea', '#9fa8da', '#ffcc80']  # Light Cyan, Periwinkle, Light Orange
colors = ['#64b5f6', '#9575cd', '#f06292']  # sky blue,Medium Purple, Pink

ppo_colour=colors[0]
prop_colour = "orange"
prop_no_action_colour = "#DA70D6"
recon_colour="red" #colors[1]
dynamics_colour="tab:green" #colors[2]
memory_colour="purple" 





franka_stack = {
    "title": "Franka Find",
    "log_dir": "franka_find",
    "legend_names": ["s1", "s4", "s8", "s32"],# , "continuous"],
    "experiment_names": ["franka_find_e2e_pt_s1", "franka_find_e2e_pt_s4", "franka_find_e2e_pt_s8", "franka_find_e2e_pt_s32"],
    "tag": "object_found_med",
    "output_file": "franka_find_object_found_med_stack.png",
    "color": ["tab:blue", "tab:red", "tab:green", "tab:green"],
    "linestyle": ['-', '-', '-', "-", "-"],
    "max_reward": 275,
    "y_max": 1,  
    "y_min": 0,
    "y_label": "object found %"  
}

franka_prop_stack = {
    "title": "Find",
    "log_dir": "part_1",
    "experiment_name": "franka_find",
    "legend_names": ["p_s16", "pt_s16",  "p_s4", "pt_s4", "p_s2", "pt_s2", "p_s1", "pt_s1",  "p_s16_no_action"],
    "run_names": ["p_s16", "pt_s16",  "p_s4", "pt_s4", "p_s2", "pt_s2", "p_s1", "pt_s1", "p_s16_no_action"],
    "tag": "mean_eval_return", # object_found_easy
    "output_file": "franka_find_part_1.png",
    "color": ["tab:blue", "tab:blue", "tab:red", "tab:red", "tab:green", "tab:green", "tab:red", "tab:red", "tab:purple", "tab:purple", "tab:brown", "tab:blue", "tab:red", "tab:green", "tab:red", "tab:purple", "tab:brown"],
    "linestyle": ['--', '-', '--', "-", "--", '-', '--', '-', '--', "-", "--", '--'],
    "marker": ['.', 'o','.', 'o','.', 'o','.', 'o','.', 'o',],
    "max_reward": 0,
    "y_max": 225,  
    "y_min": 50,
    "y_label": "%",
    "legend_loc": "upper left"
}

bounce_prop_stack = {
    "title": "Bounce",
    "log_dir": "part_1",
    "experiment_name": "shadow_bounce",
    "legend_names": ["p_s16", "pt_s16",  "p_s4", "pt_s4", "p_s2", "pt_s2", "p_s1", "pt_s1"],
    "run_names": ["p_s16", "pt_s16", "p_s4", "pt_s4", "p_s2", "pt_s2", "p_s1", "pt_s1"],
    "tag": "mean_eval_return", # object_found_easy
    "output_file": "part_1.png",
    "color": ["tab:blue", "tab:blue", "tab:red", "tab:red", "tab:green", "tab:green", "tab:red", "tab:red", "tab:purple", "tab:brown", "tab:blue", "tab:red", "tab:green", "tab:red", "tab:purple", "tab:brown"],
    "linestyle": ['--', '-', '--', "-", "--", '-', '--', '-', '--', "-", "--", '--'],
    "marker": ['.', 'o','.', 'o','.', 'o','.', 'o','.', 'o',],
    "max_reward": 0,
    "y_max": 700,  
    "y_min": -10,
    "y_label": "%",
    "legend_loc": "upper left"
}

baoding_prop_stack = {
    "title": "Baoding",
    "log_dir": "part_1",
    "experiment_name": "shadow_baoding",
    "legend_names": ["p_s16", "pt_s16",  "p_s4", "pt_s4", "p_s2", "pt_s2", "p_s1", "pt_s1"],
    "run_names": ["p_s16", "pt_s16", "p_s4", "pt_s4", "p_s2", "pt_s2", "p_s1", "pt_s1"],
    "tag": "mean_eval_return", # object_found_easy
    "output_file": "part_1.png",
    "color": ["tab:blue", "tab:blue", "tab:red", "tab:red", "tab:green", "tab:green", "tab:red", "tab:red", "tab:purple", "tab:brown", "tab:blue", "tab:red", "tab:green", "tab:red", "tab:purple", "tab:brown"],
    "linestyle": ['--', '-', '--', "-", "--", '-', '--', '-', '--', "-", "--", '--'],
    "marker": ['.', 'o','.', 'o','.', 'o','.', 'o','.', 'o',],
    "max_reward": 0,
    "y_max": 420,  
    "y_min": 0,
    "y_label": "%",
    "legend_loc": "upper left"
}


franka_recon = {
    "title": "Franka Find",
    "log_dir": "franka_find",
    "legend_names": ["PPO", "+recon"],# , "continuous"],
    "experiment_names": ["franka_find_e2e_binary_seeded", "franka_find_recon_binary_seeded"],
    "tag": "mean_eval_return",
    "output_file": "franka_find_recon.png",
    "color": ["tab:blue", "tab:red"],
    "linestyle": ['-', '-', '-'],
    "max_reward": 275,
    "y_max": 200  
}

bounce_preds = {
    "title": "Bounce",
    "log_dir": "part_2",
    "experiment_name": "shadow_bounce",
    "legend_names": ["+tactile recon", "+tactile dynamics"],
    "run_names": ["tactile_recon", "tactile_dynamics"],
    "tag": "mean_eval_return", # object_found_easy
    "color": [recon_colour, dynamics_colour, dynamics_colour, "tab:green", "tab:green", "tab:red", "tab:red", "tab:purple", "tab:brown", "tab:blue", "tab:red", "tab:green", "tab:red", "tab:purple", "tab:brown"],
    "linestyle": ['-', '-', '--', "--", "--", '-', '--', '-', '--', "-", "--", '--'],
    "max_reward": 0,
    "x_max": 199,
    "y_max": 850,  
    "y_min": 0,
    "legend_loc": "upper left",
    "output_file": "bounce_preds.png",
    "y_label": "mean"
}


# STUDY PLOTS

franka_study_mean_return = {
    "title": "Find",
    "log_dir": "logs",
    "experiment_name": "find",
    "legend_names": ["prop-tactile", "prop", "prop(no action)"],
    "run_names": ["prop_tactile", "prop", "prop_no_action"],
    "tag": "mean_eval_return", #"mean_eval_return",
    "color": [ppo_colour, prop_colour, prop_no_action_colour],
    "linestyle": ['-', '-', '-'],
    "max_reward": 0,
    "x_min": 3,
    "x_max": 199,
    "y_max": 235,  
    "y_min": 60,
    "legend_loc": "upper left",
    "y_label": "Mean evaluation return", #Mean evaluation return",
}

bounce_study = {
    "title": "Bounce",
    "log_dir": "logs",
    "experiment_name": "bounce",
    "legend_names": ["prop-tactile", "prop",  "prop(no action)"],
    "run_names": ["prop_tactile", "prop", "prop_no_action"],
    "tag": "mean_eval_return",
    "color": [ppo_colour, prop_colour, prop_no_action_colour],
    "linestyle": ['-', '-', "-"],
    "max_reward": 0,
    "x_max": 199,
    "x_min": 0,
    "y_max": 900,  
    "y_min": 0,
    "y_label": "Mean evaluation return",
    "legend_loc": "upper left"
}


baoding_study_mean_return = {
    "title": "Baoding",
    "log_dir": "logs",
    "experiment_name": "baoding",
    "legend_names": ["PPO(prop-tactile)", "PPO(prop)",  "PPO(prop(no last action))"],
    "run_names": ["prop_tactile", "prop", "prop_no_action"],
    "tag": "mean_eval_return",
    "color": [ppo_colour, prop_colour, prop_no_action_colour],
    "linestyle": ['-', '-', '-'],
    "max_reward": 0,
    "x_max": 199,
    "x_min": 0,
    "y_max": 420,  
    "y_min": 0,
    "y_label": "Mean evaluation return",
    "legend_loc": "upper left",
    "output_file": "baoding_test.png"
}

study_plot = {
    "exp_list": [franka_study_mean_return, bounce_study, baoding_study_mean_return],
    "output_file": "studying.pdf",
    "y_label": "Mean evaluation return",
    "legend_loc": "upper left",
    "opacity": 0.2,
    "legend_idx": 2
}


# SSL PLOTS
franka_ssl_mean_return = {
    "title": "Find",
    "log_dir": "logs",
    "experiment_name": "find",
    "legend_names": ["PPO(prop)", "PPO(prop-tactile)", "+Full Reconstruction (FR)", "+Tactile Reconstruction (TR)",  "+Forward Dynamics (FD)", "+Tactile Forward Dynamics (TFD)"],
    "run_names": ["prop", "prop_tactile", "recon", "tactile_recon", "dynamics", "tactile_dynamics"],
    "tag": "mean_eval_return",
    "color": [ppo_colour, prop_colour, recon_colour, recon_colour, dynamics_colour, dynamics_colour,],
    "linestyle": ['-', '-','-', '--', "-", "--"],
    "max_reward": 0,
    "x_min": 3,
    "x_max": 199,
    "y_max": 235,  
    "y_min": 90,
    "legend_loc": "upper left",
    "y_label": "Mean evaluation return",
}

bounce_ssl_mean_return = {
    "title": "Bounce",
    "log_dir": "logs",
    "experiment_name": "bounce",
    "run_names": ["prop_tactile", "prop", "recon", "tactile_recon", "dynamics", "tactile_dynamics"],
    "legend_names": ["PPO(prop)", "PPO(prop-tactile)", "+Full Reconstruction (FR)", "+Tactile Reconstruction (TR)",  "+Forward Dynamics (FD)", "+Tactile Forward Dynamics (TFD)"],
    "tag": "mean_eval_return",
    "color": [ppo_colour, prop_colour, recon_colour, recon_colour, dynamics_colour, dynamics_colour,],
    "linestyle": ['-', '-','-', '--', "-", "--"],
    "max_reward": 0,
    "x_max": 199,
    "x_min": 0,
    "y_max": 900,  
    "y_min": 0,
    "legend_loc": "upper left",
    "y_label": "Mean evaluation return",
}


baoding_ssl_mean_return = {
    "title": "Baoding",
    "log_dir": "logs",
    "experiment_name": "baoding",
    "run_names": ["prop_tactile", "prop", "recon", "tactile_recon", "dynamics", "tactile_dynamics"],
    "legend_names": ["PPO", "PPO(prop)", "+FR", "+TR", "+FD", "+TFD"],
    "tag": "mean_eval_return",
    "color": [ppo_colour, prop_colour, recon_colour, recon_colour, dynamics_colour, dynamics_colour,],
    "linestyle": ['-', '-','-', '--', "-", "--"],
    "max_reward": 0,
    "x_max": 199,
    "x_min": 0,
    "y_max": 420,  
    "y_min": 0,
    "legend_loc": "upper left",
    "y_label": "Mean evaluation return",
}

ssl_plot = {
    "exp_list": [franka_ssl_mean_return, bounce_ssl_mean_return, baoding_ssl_mean_return],
    "output_file": "ssl_mean_return_plot.pdf",
    "y_label": "Mean evaluation return",
    "legend_loc": "lower right",
    "opacity": 0.05,
    "legend_idx": 0
}

# minimal for video plot

# SSL PLOTS
franka_ppo = {
    "title": "Find",
    "log_dir": "logs",
    "experiment_name": "find",
    "legend_names": ["PPO"],
    "run_names": ["prop_tactile"],
    "tag": "mean_eval_return",
    "color": [ppo_colour, dynamics_colour, dynamics_colour,],
    "linestyle": ['-', '-'],
    "max_reward": 0,
    "x_min": 3,
    "x_max": 199,
    "y_max": 235,  
    "y_min": 90,
    "legend_loc": "upper left",
    "y_label": "Mean evaluation return",
}

bounce_ppo = {
    "title": "Bounce",
    "log_dir": "logs",
    "experiment_name": "bounce",
    "legend_names": ["PPO"],
    "run_names": ["prop_tactile"],
    "tag": "mean_eval_return",
    "color": [ppo_colour, dynamics_colour, dynamics_colour,],
    "linestyle": ['-', '-'],
    "max_reward": 0,
    "x_max": 199,
    "x_min": 0,
    "y_max": 900,  
    "y_min": 0,
    "legend_loc": "upper left",
    "y_label": "Mean evaluation return",
}

baoding_ppo = {
    "title": "Baoding",
    "log_dir": "logs",
    "experiment_name": "baoding",
    "legend_names": ["PPO"],
    "run_names": ["prop_tactile"],
    "tag": "mean_eval_return",
    "color": [ppo_colour, dynamics_colour, dynamics_colour,],
    "linestyle": ['-', '-'],
    "max_reward": 0,
    "x_max": 199,
    "x_min": 0,
    "y_max": 420,  
    "y_min": 0,
    "legend_loc": "upper left",
    "y_label": "Mean evaluation return",
}

ssl_plot_minimal = {
    "exp_list": [franka_ppo, bounce_ppo, baoding_ppo],
    "output_file": "ssl_ppo.pdf",
    "y_label": "Mean evaluation return",
    "legend_loc": "lower right",
    "opacity": 0.3,
    "legend_idx": 1
}

# MEMORY
franka_memory_mean_return = {
    "title": "Find",
    "log_dir": "logs",
    "experiment_name": "find",
    "legend_names": ["PPO(prop-tactile)", "+full dynamics", "memory"],
    "run_names": ["prop_tactile", "dynamics", "memory"],
    "tag": "mean_eval_return",
    "color": [ppo_colour, dynamics_colour, memory_colour],
    "linestyle": ['-', '-', '-'],
    "max_reward": 0,
    "x_min": 3,
    "x_max": 199,
    "y_max": 235,  
    "y_min": 90,
    "legend_loc": "upper left",
    "y_label": "Mean evaluation return",
}

bounce_memory_mean_return = {
    "title": "Bounce",
    "log_dir": "logs",
    "experiment_name": "bounce",
    "legend_names": ["PPO(prop-tactile)", "+Forward Dynamics (FD)", r"+FD+$N_{rollouts}$"],
    "run_names": ["prop_tactile", "dynamics", "memory"],
    "tag": "mean_eval_return",
    "color": [ppo_colour, dynamics_colour, memory_colour],
    "linestyle": ['-', '-', '-'],
    "max_reward": 0,
    "x_max": 199,
    "x_min": 0,
    "y_max": 900,  
    "y_min": 0,
    "legend_loc": "upper left",
    "y_label": "Mean evaluation return",
}

baoding_memory_mean_return = {
    "title": "Baoding",
    "log_dir": "logs",
    "experiment_name": "baoding",
    "legend_names": ["PPO(prop-tactile)", "+FD", r"$N_{rollouts}$"],
    "run_names": ["prop_tactile", "dynamics", "memory"],
    "tag": "mean_eval_return",
    "color": [ppo_colour, dynamics_colour, memory_colour],
    "linestyle": ['-', '-', '-'],
    "max_reward": 0,
    "x_max": 199,
    "x_min": 0,
    "y_max": 500,  
    "y_min": 0,
    "legend_loc": "upper left",
    "y_label": "Mean evaluation return",
}

memory_plot = {
    "exp_list": [franka_memory_mean_return, bounce_memory_mean_return, baoding_memory_mean_return],
    "output_file": "memory_mean_return_plot.pdf",
    "y_label": "Mean evaluation return",
    "legend_loc": "lower right",
    "opacity": 0.08,
    "legend_idx": 1
}

# bar chart

baoding_ssl_rotations_barchart = {
    "title": "Mean and maximum complete rotations in Baoding",
    "log_dir": "logs",
    "experiment_name": "baoding",
    "legend_names": ["PPO(prop)", "PPO(prop-tactile)", "+full recon", "+tac recon", "+full dyn", "+memory"],
    "run_names": ["prop", "prop_tactile", "recon", "tactile_recon", "dynamics", "tactile_dynamics", "memory"],
    "tag": "num_rotations",
    "color": [prop_colour, ppo_colour, recon_colour, recon_colour, dynamics_colour, memory_colour],
    "linestyle": ['-', '-','-', '--', "-", "--", '-', '--', '-', '--', "-", "--", '--'],
    "max_reward": 0,
    "bar_chart": True,
    "x_max": 199,
    "x_min": 0,
    "y_max": 25,  
    "y_min": 0,
    "legend_loc": "upper left",
    "y_label": "Maximum complete rotations",
    "output_file": "num_rotations_barchart.pdf"
}

bounce_ssl_rotations_barchart = {
    "title": "Mean and maximum complete rotations in Baoding",
    "log_dir": "logs",
    "experiment_name": "bounce",
    "legend_names": ["PPO(prop)","PPO(prop-tactile)", "+recon", "+tactile recon", "+dynamics", "memory"],
    "run_names": ["prop", "prop_tactile", "recon", "tactile_recon", "dynamics", "tactile_dynamics", "memory"],
    "tag": "bounce_reward",
    "color": [prop_colour, ppo_colour, recon_colour, recon_colour, dynamics_colour, memory_colour],
    "linestyle": ['-', '-','-', '--', "-", "--", '-', '--', '-', '--', "-", "--", '--'],
    "max_reward": 0,
    "bar_chart": True,
    "y_max": 90,  
    "y_min": 50,
    "legend_loc": "upper left",
    "y_label": "Maximum complete rotations",
    "output_file": "num_bounces_barchart.pdf"
}

franka_barchart = {
    "title": "Mean and maximum complete rotations in Baoding",
    "log_dir": "logs",
    "experiment_name": "find",
    "legend_names": ["PPO(prop)", "PPO(prop-tactile)", "+full recon", "+tactile recon",  "+full dynamics", "+memory"],
    "run_names": ["prop", "prop_tactile", "recon", "tactile_recon", "dynamics", "tactile_dynamics", "memory"],
    "tag": "timesteps_to_find_object_med",
    "color": [prop_colour, ppo_colour, recon_colour, recon_colour, dynamics_colour, memory_colour],
    "linestyle": ['-', '-','-', '--', "-", "--", '-', '--', '-', '--', "-", "--", '--'],
    "max_reward": 0,
    "bar_chart": True,
    "y_max": 3.9,  
    "y_min": 2.7,
    "legend_loc": "upper left",
    "y_label": "Maximum complete rotations",
    "output_file": "franka_barchart.pdf"
}


# FRANKA TIMESTEPS
franka_ssl_timesteps = {
    "title": "within 1cm",
    "log_dir": "logs",
    "experiment_name": "find",
    "legend_names": ["PPO(prop)", "PPO(prop-tactile)", "+Full Reconstruction (FR)", "+Tactile Reconstruction (TR)",  "+Forward Dynamics (FD)", "+Tactile Forward Dynamics (TFD)"],
    "run_names": ["prop", "prop_tactile", "recon", "tactile_recon", "dynamics", "tactile_dynamics"],
    "tag": "timesteps_to_find_object_med",
    "color": [ppo_colour, prop_colour, recon_colour, recon_colour, dynamics_colour, dynamics_colour,],
    "linestyle": ['-', '-','-', '--', "-", "--"],
    "max_reward": 0,
    "x_min": 5,
    "x_max": 199,
    "y_max": 5,  
    "y_min": 1,
    "legend_loc": "upper left",
    "y_label": "Seconds to find object", #Mean evaluation return",
}
franka_ssl_timesteps_easy = {
    "title": "within 3cm",
    "log_dir": "logs",
    "experiment_name": "find",
    "legend_names": ["PPO(prop)", "PPO(prop-tactile)", "+Full Reconstruction (FR)", "+Tactile Reconstruction (TR)",  "+Forward Dynamics (FD)", "+Tactile Forward Dynamics (TFD)"],
    "run_names": ["prop", "prop_tactile", "recon", "tactile_recon", "dynamics", "tactile_dynamics"],
    "tag": "timesteps_to_find_object_easy",
    "color": [ppo_colour, prop_colour, recon_colour, recon_colour, dynamics_colour, dynamics_colour,],
    "linestyle": ['-', '-','-', '--', "-", "--"],
    "max_reward": 0,
    "x_min": 5,
    "x_max": 199,
    "y_max": 5,  
    "y_min": 1,
    "legend_loc": "upper left",
    "y_label": "Seconds to find object", #Mean evaluation return",
}

franka_ssl_timesteps_hard = {
    "title": "within 0.05cm",
    "log_dir": "logs",
    "experiment_name": "find",
    "legend_names": ["PPO(prop)", "PPO(prop-tactile)", "+Full Reconstruction (FR)", "+Tactile Reconstruction (TR)",  "+Forward Dynamics (FD)", "+Tactile Forward Dynamics (TFD)"],
    "run_names": ["prop", "prop_tactile", "recon", "tactile_recon", "dynamics", "tactile_dynamics"],
    "tag": "timesteps_to_find_object_hard",
    "color": [ppo_colour, prop_colour, recon_colour, recon_colour, dynamics_colour, dynamics_colour,],
    "linestyle": ['-', '-','-', '--', "-", "--"],
    "max_reward": 0,
    "x_min": 5,
    "x_max": 199,
    "y_max": 5,  
    "y_min": 1,
    "legend_loc": "upper left",
    "y_label": "Seconds to find object", #Mean evaluation return",
}

franka_extra_plot = {
    "exp_list": [franka_ssl_timesteps_easy, franka_ssl_timesteps, franka_ssl_timesteps_hard],
    "output_file": "franka_extra_plot.pdf",
    "y_label": "Seconds to find object",
    "legend_loc": "upper right",
    "opacity": 0.08,
    "legend_idx": 0
}

## BOUNCES

bounce_ssl_bounces = {
    "title": "Number of bounces",
    "log_dir": "logs",
    "experiment_name": "bounce",
    "legend_names": ["PPO(prop)", "PPO(prop-tactile)", "+Full Reconstruction (FR)", "+Tactile Reconstruction (TR)",  "+Forward Dynamics (FD)", "+Tactile Forward Dynamics (TFD)"],
    "run_names": ["prop", "prop_tactile", "recon", "tactile_recon", "dynamics", "tactile_dynamics"],
    "tag": "bounce_reward", # object_found_easy
    "color": [ppo_colour, prop_colour, recon_colour, recon_colour, dynamics_colour, dynamics_colour,],
    "linestyle": ['-', '-','-', '--', "-", "--"],
    "max_reward": 0,
    "x_max": 199,
    "x_min": 0,
    "y_max": 85,  
    "y_min": 0,
    "legend_loc": "lower right",
    "title": r"Number of bounces",
    "x_label": "Timesteps (M)",
    "y_label": "Number of bounces",
    "output_file": "num_bounces.pdf"

}

## NUM ROTATIONS

baoding_ssl_rotations = {
    "title": "Number of Baoding rotations (all seeds)",
    "log_dir": "logs",
    "experiment_name": "baoding",
    "legend_names": ["PPO(prop)", "PPO(prop-tactile)", "+Full Reconstruction (FR)", "+Tactile Reconstruction (TR)",  "+Forward Dynamics (FD)", "+Tactile Forward Dynamics (TFD)"],
    "run_names": ["prop", "prop_tactile", "recon", "tactile_recon", "dynamics", "tactile_dynamics"],
    "tag": "num_rotations",
    "color": [prop_colour, ppo_colour, recon_colour, recon_colour, dynamics_colour, dynamics_colour,  "tab:red", "tab:green", "tab:green", "tab:red", "tab:red", "tab:purple", "tab:brown", "tab:blue", "tab:red", "tab:green", "tab:red", "tab:purple", "tab:brown"],
    "linestyle": ['-', '-','-', '--', "-", "--", '-', '--', '-', '--', "-", "--", '--'],
    "max_reward": 0,
    "x_max": 199,
    "x_min": 0,
    "y_max": 17,  
    "y_min": -1,
    "legend_loc": "upper left",
    "y_label": "Complete rotations",
    "x_label": "Timesteps (M)",
    "output_file": "num_rotations.pdf"
}

baoding_ssl_rotations_minimal = {
    "title": "Number of Baoding rotations (minimal, all seeds)",
    "log_dir": "logs",
    "experiment_name": "baoding",
    "legend_names": ["PPO(prop-tactile)", "+tactile recon", "+full dynamics"],
    "run_names": ["prop_tactile", "tactile_recon", "dynamics"],
    "tag": "num_rotations",
    "color": [ppo_colour, recon_colour, dynamics_colour],
    "linestyle": ['-', '--','-'],
    "max_reward": 0,
    "x_max": 199,
    "x_min": 0,
    "y_max": 17,  
    "y_min": -1,
    "legend_loc": "upper left",
    "y_label": "Complete rotations",
    "x_label": "Timesteps (M)",
    "output_file": "num_rotations_minimal.pdf"
}

baoding_ssl_rotations_minimal_good = {
    "title": "Number of Baoding rotations (minimal, no bad seeds)",
    "log_dir": "logs",
    "experiment_name": "baoding_good",
    "legend_names": ["PPO(prop-tactile)", "+tactile recon", "+full dynamics"],
    "run_names": ["prop_tactile", "tactile_recon", "dynamics"],
    "tag": "num_rotations",
    "color": [ppo_colour, recon_colour, dynamics_colour],
    "linestyle": ['-', '--','-'],
    "max_reward": 0,
    "x_max": 199,
    "x_min": 0,
    "y_max": 17,  
    "y_min": -1,
    "legend_loc": "upper left",
    "y_label": "Complete rotations",
    "x_label": "Timesteps (M)",
    "output_file": "num_rotations_minimal_good.pdf"
}

baoding_ssl_rotations_good = {
    "title": "Number of Baoding rotations (no bad seeds)",
    "log_dir": "logs",
    "experiment_name": "baoding_good",
    "legend_names": ["PPO(prop)", "PPO(prop-tactile)", "+full recon", "+tactile recon", "+full dynamics", "+tactile dynamics"],
    "run_names": ["prop", "prop_tactile", "recon", "tactile_recon", "dynamics", "tactile_dynamics"],
    "tag": "num_rotations",
    "color": [prop_colour, ppo_colour, recon_colour, recon_colour, dynamics_colour, dynamics_colour,  "tab:red", "tab:green", "tab:green", "tab:red", "tab:red", "tab:purple", "tab:brown", "tab:blue", "tab:red", "tab:green", "tab:red", "tab:purple", "tab:brown"],
    "linestyle": ['-', '-','-', '--', "-", "--", '-', '--', '-', '--', "-", "--", '--'],
    "max_reward": 0,
    "x_max": 199,
    "x_min": 0,
    "y_max": 17,  
    "y_min": -1,
    "legend_loc": "upper left",
    "y_label": "Complete rotations",
    "x_label": "Timesteps (M)",
    "output_file": "num_rotations_good.pdf"
}

######

franka_ssl_mean_return_camready = {
    "title": "Find",
    "log_dir": "ssl",
    "experiment_name": "find",
    "legend_names": ["PPO(prop-tactile)", "+tactile recon",  "+full dynamics", "+tactile dynamics"],
    "run_names": ["pt"],
    "tag": "mean_eval_return",
    "color": [ppo_colour, recon_colour],
    "linestyle": ['-', '--'],
    "max_reward": 0,
    "x_min": 3,
    "x_max": 199,
    "y_max": 600,  
    "y_min": 0,
    "legend_loc": "upper left",
    "y_label": "Mean evaluation return",
}

bounce_ssl_mean_return_camready = {
    "title": "Bounce",
    "log_dir": "ssl",
    "experiment_name": "bounce",
    "legend_names": ["PPO(prop-tactile)", "+tactile recon",  "+full dynamics", "+tactile dynamics"],
    "run_names": ["pt", "tac_recon", "dynamics"],
    "tag": "mean_eval_return",
    "color": [ppo_colour, recon_colour, dynamics_colour],
    "linestyle": ['-', '--', '-'],
    "max_reward": 0,
    "x_min": 3,
    "x_max": 199,
    "y_max": 800,  
    "y_min": 0,
    "legend_loc": "upper left",
    "y_label": "Mean evaluation return",
}

baoding_ssl_mean_return_camready = {
    "title": "Baoding",
    "log_dir": "ssl",
    "experiment_name": "baoding",
    "legend_names": ["PPO(prop-tactile)", "+tactile recon",  "+full dynamics", "+tactile dynamics"],
    "run_names": ["pt", "tac_recon", "dynamics"],
    "tag": "mean_eval_return",
    "color": [ppo_colour, recon_colour, dynamics_colour],
    "linestyle": ['-', '--', '-'],
    "max_reward": 0,
    "x_min": 3,
    "x_max": 199,
    "y_max": 400,  
    "y_min": 0,
    "legend_loc": "upper left",
    "y_label": "Mean evaluation return",
}


bounce_sweep_example = {
    "title": "Bounce (+ full dynamics) sweep",
    "log_dir": "appendix",
    "experiment_name": "sweep_example",
    "legend_names": ["PPO"],
    "run_names": ["bounce_dynamics"],
    "tag": "mean_eval_return", # object_found_easy
    "color": [ppo_colour, prop_colour, recon_colour, recon_colour, dynamics_colour,  dynamics_colour, "purple", "tab:brown", "tab:blue", "tab:red", "tab:green", "tab:red", "tab:purple", "tab:brown"],
    "linestyle": ['-', '-', '-', '--', "-", "--", '-', '--', '-', '--', "-", "--", '--'],
    "max_reward": 0,
    "x_max": 199,
    "x_min": 0,
    "y_max": 900,  
    "y_min": 0,
    "legend_loc": "upper left",
    "y_label": "Mean evaluation return",
    "output_file": "example_sweep.pdf"
}

tp_rate = {
    "title": "TP rate",
    "log_dir": "appendix",
    "experiment_name": "tactile_dynamics",
    "legend_names": ["Find", "Bounce", "Baoding"],
    "run_names": ["franka_find", "shadow_bounce", "shadow_baoding"],
    "tags": ["Tactile / true_positive_rate @t=0", "Tactile / true_positive_rate @t=1", "Tactile / true_positive_rate @t=2", "Tactile / true_positive_rate @t=8"], # object_found_easy
    "color": [dynamics_colour, ppo_colour, recon_colour],
    "linestyle": ['-', '-', '-', '-', "-", "--", '-', '--', '-', '--', "-", "--", '--'],
    "max_reward": 0,
    "x_max": 700,
    "x_min": 0,
    "y_max": 1,  
    "y_min": 0.88,
    "legend_loc": "upper right",
    "x_label": "Number of rollouts",
    # "y_label": "Mean evaluation return",
    "output_file": "all_tacdyn_tp_rate.pdf"
}

bounce_fp_rate = {
    "title": "FP rate",
    "log_dir": "appendix",
    "experiment_name": "shadow_bounce",
    "legend_names": [r"$t=1$", r"$t=2$", r"$t=3$", r"$t=9$"],
    "run_names": ["tactile_dynamics"],
    "tags": ["Tactile / false_positive_rate @t=0", "Tactile / false_positive_rate @t=1", "Tactile / false_positive_rate @t=2", "Tactile / false_positive_rate @t=8"], # object_found_easy
    "color": [ppo_colour],
    "linestyle": ['-', '-', '-', '-', "-", "--", '-', '--', '-', '--', "-", "--", '--'],
    "max_reward": 0,
    "x_max": 700,
    "x_min": 0,
    "y_max": 0.3,  
    "y_min": 0.05,
    "legend_loc": "upper right",
    "x_label": "Number of rollouts",
    # "y_label": "Mean evaluation return",
    "output_file": "bounce_tacdyn_fp_rate.pdf"
}

bounce_fn_rate = {
    "title": "FN rate",
    "log_dir": "appendix",
    "experiment_name": "shadow_bounce",
    "legend_names": [r"$t=1$", r"$t=2$", r"$t=3$", r"$t=9$"],
    "run_names": ["tactile_dynamics"],
    "tags": ["Tactile / false_negative_rate @t=0", "Tactile / false_negative_rate @t=1", "Tactile / false_negative_rate @t=2", "Tactile / false_negative_rate @t=8"], # object_found_easy
    "color": [ppo_colour],
    "linestyle": ['-', '-', '-', '-', "-", "--", '-', '--', '-', '--', "-", "--", '--'],
    "max_reward": 0,
    "x_max": 700,
    "x_min": 0,
    "y_max": 0.005,  
    "y_min": 0.001,
    "legend_loc": "upper right",
    "x_label": "Number of rollouts",
    # "y_label": "Mean evaluation return",
    "output_file": "bounce_tacdyn_fn_rate.pdf"
}

bounce_tn_rate = {
    "title": "TN rate",
    "log_dir": "appendix",
    "experiment_name": "shadow_bounce",
    "legend_names": [r"$t=1$", r"$t=2$", r"$t=3$", r"$t=9$"],
    "run_names": ["tactile_dynamics"],
    "tags": ["Tactile / true_negative_rate @t=0", "Tactile / true_negative_rate @t=1", "Tactile / true_negative_rate @t=2", "Tactile / true_negative_rate @t=8"], # object_found_easy
    "color": [ppo_colour],
    "linestyle": ['-', '-', '-', '-', "-", "--", '-', '--', '-', '--', "-", "--", '--'],
    "max_reward": 0,
    "x_max": 700,
    "x_min": 0,
    "y_max": 1,  
    "y_min": 0.96,
    "legend_loc": "lower right",
    "x_label": "Number of rollouts",
    # "y_label": "Mean evaluation return",
    "output_file": "bounce_tacdyn_tn_rate.pdf"
}

bounce_accuracy = {
    "title": "Accuracy",
    "log_dir": "appendix",
    "experiment_name": "shadow_bounce",
    "legend_names": [r"$t=1$", r"$t=2$", r"$t=3$", r"$t=9$"],
    "run_names": ["tactile_dynamics"],
    "tags": ["Tactile / accuracy @t=0", "Tactile / accuracy @t=1", "Tactile / accuracy @t=2", "Tactile / accuracy @t=8"], # object_found_easy
    "color": [ppo_colour],
    "linestyle": ['-', '-', '-', '-', "-", "--", '-', '--', '-', '--', "-", "--", '--'],
    "max_reward": 0,
    "x_max": 700,
    "x_min": 0,
    "y_max": 1,  
    "y_min": 0.96,
    "legend_loc": "lower right",
    "x_label": "Number of rollouts",
    # "y_label": "Mean evaluation return",
    "output_file": "bounce_tacdyn_accuracy.pdf"
}

bounce_f1 = {
    "title": "F1",
    "log_dir": "appendix",
    "experiment_name": "shadow_bounce",
    "legend_names": [r"$t=1$", r"$t=2$", r"$t=3$", r"$t=9$"],
    "run_names": ["tactile_dynamics"],
    "tags": ["Tactile / f1 @t=0", "Tactile / f1 @t=1", "Tactile / f1 @t=2", "Tactile / f1 @t=8"], # object_found_easy
    "color": [ppo_colour],
    "linestyle": ['-', '-', '-', '-', "-", "--", '-', '--', '-', '--', "-", "--", '--'],
    "max_reward": 0,
    "x_max": 700,
    "x_min": 0,
    "y_max": 0.96,  
    "y_min": 0.84,
    "legend_loc": "upper right",
    "x_label": "Number of rollouts",
    # "y_label": "Mean evaluation return",
    "output_file": "bounce_tacdyn_f1.pdf"
}

aux_loss_example = {
    "title": "Bounce preds",
    "log_dir": "appendix",
    "experiment_name": "shadow_bounce",
    "legend_names": ["0", "1", "2"],
    "run_names": ["tactile_dynamics"],
    "tag": "aux_loss", #tp_rate@t=0", "tp_rate@t=1", "tp_rate@t=2"], # object_found_easy
    "color": [ppo_colour],
    "linestyle": ['-', '-', '-', '--', "-", "--", '-', '--', '-', '--', "-", "--", '--'],
    "max_reward": 0,
    "x_max": 150,
    "x_min": 60,
    "y_max": 1.9,  
    "y_min": 1.7,
    "legend_loc": "upper left",
    "y_label": "Average auxiliary loss",
    "output_file": "aux_loss.png"
}




bounce_tactile_preds = {
    "title": "Bounce",
    "log_dir": "part_2",
    "experiment_name": "shadow_bounce",
    "legend_names": ["+tactile recon", "+dynamics", "+tactile dynamics"],
    "run_names": ["tactile_dynamics"],
    "tag": "true_positive_weight @t=0", # object_found_easy
    "color": [ppo_colour, prop_colour, recon_colour, recon_colour, dynamics_colour,  dynamics_colour, dynamics_colour, "tab:green", "tab:green", "tab:red", "tab:red", "tab:purple", "tab:brown", "tab:blue", "tab:red", "tab:green", "tab:red", "tab:purple", "tab:brown"],
    "linestyle": ['-', '-', '-', '--', "-", "--", '-', '--', '-', '--', "-", "--", '--'],
    "max_reward": 0,
    "x_max": 199,
    "x_min": 0,
    "y_max": 900,  
    "y_min": 0,
    "legend_loc": "upper left",
    "y_label": "Mean evaluation return",
    "output_file": "pred.pdf",

}





combo_plot = {
    "exp_list": [franka_prop_stack, bounce_prop_stack, baoding_prop_stack],
    "output_file": "prop.pdf",
    "y_label": "Mean evaluation return",
    "legend_loc": "lower right",
}




