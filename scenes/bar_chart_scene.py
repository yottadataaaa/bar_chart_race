import pandas as pd
import numpy as np
from manim import *

from utils.bar_chart_race_runner import BarChartRaceRunner

class BarChartScene(Scene):
    def __init__(self, runner: "BarChartRaceRunner", **kwargs):
        self.runner = runner
        super().__init__(**kwargs)

    def construct(self):
        df = pd.read_csv(self.runner.csv_path)
        df[self.runner.time_column] = pd.to_datetime(df[self.runner.time_column])

        # 時系列順に並び替え
        df.sort_values(by=self.runner.time_column, inplace=True)
        unique_times = df[self.runner.time_column].drop_duplicates().sort_values()
        time_frames = list(unique_times)

        id_list = df[self.runner.id_column].unique().tolist()

        bar_width = 0.8
        bar_spacing = 1.2
        max_bar_value = df[self.runner.value_column].max()

        # 初期バー表示（0で初期化）
        bars = {}
        bar_labels = {}
        for i, id_ in enumerate(id_list[:self.runner.n_bars]):
            bar = Rectangle(
                width=0,
                height=bar_width,
                fill_color=self.runner.color_map.get(id_, BLUE),
                fill_opacity=0.8
            ).move_to(LEFT * 6 + DOWN * i * bar_spacing)
            bars[id_] = bar
            self.add(bar)

            label = Text(id_, font=self.runner.font_path or "Arial", font_size=24)
            label.next_to(bar, LEFT)
            bar_labels[id_] = label
            self.add(label)

        # 時系列で更新
        for t in time_frames:
            frame_df = df[df[self.runner.time_column] == t]
            top_items = (
                frame_df
                .groupby(self.runner.id_column)[self.runner.value_column]
                .sum()
                .sort_values(ascending=False)
                .head(self.runner.n_bars)
            )

            animations = []
            for i, (id_, val) in enumerate(top_items.items()):
                width_ratio = val / max_bar_value
                new_width = width_ratio * 10 

                if id_ not in bars:
                    continue

                animations.append(bars[id_].animate.set(width=new_width).move_to(LEFT * (6 - new_width / 2) + DOWN * i * bar_spacing))
                animations.append(bar_labels[id_].animate.move_to(LEFT * 6.5 + DOWN * i * bar_spacing))

            self.play(*animations, run_time=1 / self.runner.fps)


