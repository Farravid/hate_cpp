#include <benchmark/benchmark.h>

static void BM_SomeFunctionX(benchmark::State& state) {
  // Perform setup here
  for (auto _ : state) {
    // This code gets timed
    const auto s = {"Hey"};
  }
}

// Register the function as a benchmark
BENCHMARK(BM_SomeFunctionX);
// Run the benchmark
BENCHMARK_MAIN();