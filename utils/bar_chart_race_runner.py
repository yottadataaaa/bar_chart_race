from scenes.bar_chart_scene import BarChartScene
from manim import *

class BarChartRaceRunner:
    def __init__(
        self,
        csv_path: str,
        value_column: str,
        id_column: str,
        time_column: str,
        image_map: dict,
        color_map: dict,
        width_px: int,
        height_px: int,
        fps: int,
        duration_s: float,
        n_bars: int,
        interpolate: bool,
        output_file: str,
        font_path: str
    ):
        assert(csv_path is not None)
        assert(value_column is not None)
        assert(id_column is not None)
        assert(time_column is not None)

        self.csv_path = csv_path
        self.value_column = value_column
        self.id_column = id_column
        self.time_column = time_column
        self.image_map = image_map
        self.color_map = color_map
        self.width_px = width_px
        self.height_px = height_px
        self.fps = fps
        self.duration_s = duration_s
        self.n_bars = n_bars
        self.interpolate = interpolate
        self.output_file = output_file
        self.font_path = font_path

    def run(self):
        config.pixel_width = self.width_px
        config.pixel_height = self.height_px
        config.frame_rate = self.fps
        config.background_color = WHITE
        config.output_file = self.output_file
        config.renderer = "opengl"

        from manim import Scene
        scene = BarChartScene(self)
        scene.render()

