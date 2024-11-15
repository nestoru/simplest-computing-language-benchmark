GO_CODE = """
package main

import (
    "encoding/json"
    "fmt"
    "math"
    "sort"
    "strings"
    "time"
)

func arraySum() {
    arr := make([]int, 1000000)
    for i := range arr {
        arr[i] = i
    }
    sum := 0
    for _, x := range arr {
        sum += x * 2
    }
}

func stringConcat() string {
    // Test 1: String building
    var parts []string
    for i := 0; i < 10000; i++ {
        parts = append(parts, fmt.Sprintf("%dhello", i))
    }
    result1 := strings.Join(parts, "")

    // Test 2: String splitting and processing
    text := strings.Repeat("hello,world,this,is,a,test", 1000)
    words := strings.Split(text, ",")
    processed := make([]string, len(words))
    for i, word := range words {
        processed[i] = strings.ToUpper(word)
    }
    result2 := strings.Join(processed, ",")

    // Test 3: String replacements
    template := strings.Repeat("The quick brown fox", 100)
    result3 := strings.ReplaceAll(template, "quick", "slow")
    result3 = strings.ReplaceAll(result3, "brown", "red")
    result3 = strings.ReplaceAll(result3, "fox", "dog")

    return result1 + result2 + result3
}

func mathOps() {
    sum := 0.0
    for i := 0; i < 10000; i++ {
        sum += math.Sqrt(float64(i)) + math.Sin(float64(i))
    }
}

func median(numbers []float64) float64 {
    sort.Float64s(numbers)
    middle := len(numbers) / 2
    if len(numbers)%2 == 0 {
        return (numbers[middle-1] + numbers[middle]) / 2
    }
    return numbers[middle]
}

func main() {
    // Warm-up phase
    for i := 0; i < 10; i++ {
        arraySum()
        stringConcat()
        mathOps()
    }

    iterations := 1000
    arrayTimes := make([]float64, iterations)
    stringTimes := make([]float64, iterations)
    mathTimes := make([]float64, iterations)

    for i := 0; i < iterations; i++ {
        start := time.Now()
        arraySum()
        duration := time.Since(start)
        arrayTimes[i] = duration.Seconds()

        start = time.Now()
        stringConcat()
        duration = time.Since(start)
        stringTimes[i] = duration.Seconds()

        start = time.Now()
        mathOps()
        duration = time.Since(start)
        mathTimes[i] = duration.Seconds()
    }

    results := map[string]float64{
        "go_array_sum":     median(arrayTimes),
        "go_string_concat": median(stringTimes),
        "go_math":         median(mathTimes),
    }

    jsonResults, _ := json.Marshal(results)
    fmt.Println(string(jsonResults))
}
"""
