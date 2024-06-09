import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class PlotDrawer:
    def __init__(self, json_file):
        self.json_file = json_file

    @property
    def draw_plots(self):
        df = pd.read_json(self.json_file)

        os.makedirs('plots', exist_ok=True)
        os.chdir('plots')
        file_paths = []
        k = 0
        for name, values in df.items():
            if k > 1:
                plt.figure()
                plt.suptitle(f'gt_corners & {name}')
                plt.subplots_adjust(wspace=0.3)
                plt.subplot(1, 2, 1)
                plt.plot(df['gt_corners'], values, 'bo')
                plt.xlabel('gt_corners')
                plt.ylabel(name)
                plt.subplot(1, 2, 2)
                sns.histplot(data=df, x='gt_corners', y=name)
                plt.savefig(f'plot_{k - 2}.png')
            k += 1
        os.chdir('..')
        if os.path.exists('plots') and os.path.isdir('plots'):
            for root, dirs, files in os.walk('plots'):
                for file in files:
                    file_paths.append(os.path.join(root, file))

        return file_paths
