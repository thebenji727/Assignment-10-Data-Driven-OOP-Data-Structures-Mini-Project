from collections import defaultdict

class Analyzer:
    def analyze(self, records):
        grouped = defaultdict(int)

        for r in records:
            day = r.time.date()
            grouped[day] += 1

        avg_daily = sum(grouped.values()) / len(grouped)
        burst_days = [day for day, count in grouped.items() if count > avg_daily]

        conclusion = (
            "Supported"
            if len(burst_days) > len(grouped) * 0.3
            else "Not Supported"
        )

        return AnalysisResult(avg_daily, burst_days, conclusion)