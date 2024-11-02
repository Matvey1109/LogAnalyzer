from src.stats.stats_data import StatsData
from src.stats.stats_writers.stats_writer import IStatsWriter


class MarkdownStatsWriter(IStatsWriter):
    """
    A class to write statistics data to a markdown file
    """

    def __init__(self, stats_data: StatsData, file_path: str) -> None:
        """Initialize the MarkdownStatsWriter"""
        super().__init__(stats_data, file_path)

    def write_stats_to_file(self) -> None:
        """Method to write stats_data in a file"""
        with open(self._file_path, "w") as file:
            file.write("## Logs Stats Data\n\n")
            file.write("| Statistic | Value |\n")
            file.write("| --- | --- |\n")

            file.write(f"| Total Requests | {self._stats_data.total_requests} |\n")

            file.write("| Most Frequent Requested Sources | \n")
            for source, count in self._stats_data.most_frequent_requested_sources:
                file.write(f"| Source: {source} | Count: {count} |\n")

            file.write("| Most Frequent Occurring Status Codes | \n")
            for status, count in self._stats_data.most_frequent_occurring_status_codes:
                file.write(f"| Status Code: {status} | Count: {count} |\n")

            file.write(
                f"| Average Size of Response | {self._stats_data.avg_size_of_response} |\n"
            )
            file.write(
                f"| 95th Percentile of Response Size | {self._stats_data.percentile_95th_of_response_size} |\n"
            )
            file.write(f"| From Time | {self._stats_data.from_time} |\n")
            file.write(f"| To Time | {self._stats_data.to_time} |\n")

    def get_file_extension(self) -> str:
        """Method to get file extension"""
        return ".md"
