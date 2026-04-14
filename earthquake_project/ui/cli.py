class CLI:
    def display(self, result):
        print("THESIS")
        print("Earthquakes above magnitude 3.0 occur in bursts.\n")

        print("RESULTS")
        print(f"Average daily earthquakes: {result.avg_daily:.2f}")
        print(f"Burst days: {len(result.burst_days)}")

        print("\nCONCLUSION")
        print(result.conclusion)