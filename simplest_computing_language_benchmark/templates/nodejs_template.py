NODEJS_CODE = """
function arraySum() {
    const arr = Array(1000000).fill().map((_, i) => i);
    let sum = 0;
    for (const x of arr) {
        sum += x * 2;
    }
}

function stringConcat() {
    // Test 1: String building
    const parts = [];
    for (let i = 0; i < 10000; i++) {
        parts.push(`${i}hello`);
    }
    const result1 = parts.join('');
    
    // Test 2: String splitting and processing
    const text = "hello,world,this,is,a,test".repeat(1000);
    const words = text.split(",");
    const processed = words.map(word => word.toUpperCase());
    const result2 = processed.join(",");
    
    // Test 3: String replacements
    const template = "The quick brown fox".repeat(100);
    const result3 = template.replace(/quick/g, "slow")
                          .replace(/brown/g, "red")
                          .replace(/fox/g, "dog");
    
    return result1 + result2 + result3;
}

function mathOps() {
    let sum = 0;
    for (let i = 0; i < 10000; i++) {
        sum += Math.sqrt(i) + Math.sin(i);
    }
}

// Warm-up phase
for (let i = 0; i < 10; i++) {
    arraySum();
    stringConcat();
    mathOps();
}

// Benchmarking
const iterations = 1000;
const arrayTimes = [];
const stringTimes = [];
const mathTimes = [];

for (let i = 0; i < iterations; i++) {
    let start = process.hrtime.bigint();
    arraySum();
    let end = process.hrtime.bigint();
    arrayTimes.push(Number(end - start) / 1e9);

    start = process.hrtime.bigint();
    stringConcat();
    end = process.hrtime.bigint();
    stringTimes.push(Number(end - start) / 1e9);

    start = process.hrtime.bigint();
    mathOps();
    end = process.hrtime.bigint();
    mathTimes.push(Number(end - start) / 1e9);
}

function median(arr) {
    arr.sort((a, b) => a - b);
    const mid = Math.floor(arr.length / 2);
    if (arr.length % 2 === 0) {
        return (arr[mid - 1] + arr[mid]) / 2;
    }
    return arr[mid];
}

const results = {
    nodejs_array_sum: median(arrayTimes),
    nodejs_string_concat: median(stringTimes),
    nodejs_math: median(mathTimes)
};

console.log(JSON.stringify(results));
"""
