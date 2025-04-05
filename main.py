import argparse
import json 
from pathlib import Path
from utils.bar_chart_race_runner import BarChartRaceRunner

def load_json_if_provided(path_str) -> dict:
    if path_str:
        path = Path(path_str)
        if path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            print(f"[警告] JSONファイルが見つかりません: {path_str}")
    return None

def parse_args():
    parser = argparse.ArgumentParser(description="Bar Chart Race Generator")

    parser.add_argument("--csv_path", type=str, required=True)
    parser.add_argument("--value_column", type=str, required=True)
    parser.add_argument("--id_column", type=str, required=True)
    parser.add_argument("--time_column", type=str, required=True)

    parser.add_argument("--image_map_path", type=str, default=None)
    parser.add_argument("--color_map_path", type=str, default=None)

    parser.add_argument("--width_px", type=int, default=1920)
    parser.add_argument("--height_px", type=int, default=1080)
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--duration_s", type=float, default=None)
    parser.add_argument("--n_bars", type=int, default=10)
    parser.add_argument("--interpolate", action="store_true")
    parser.add_argument("--output_file", type=str, default="output.mp4")
    parser.add_argument("--font_path", type=str, default=None)

    return parser.parse_args()

def main():
    args = parse_args()

    image_map = load_json_if_provided(args.image_map_path)
    color_map = load_json_if_provided(args.color_map_path)

    runner = BarChartRaceRunner(
        csv_path=args.csv_path,
        value_column=args.value_column,
        id_column=args.id_column,
        time_column=args.time_column,
        image_map=image_map,
        color_map=color_map,
        width_px=args.width_px,
        height_px=args.height_px,
        fps=args.fps,
        duration_s=args.duration_s,
        n_bars=args.n_bars,
        interpolate=args.interpolate,
        output_path=args.output,
        font_path=args.font_path,
    )

    runner.run()

if __name__ == "__main__":
    main()