ocument.body.append(document.createElement('textarea'));
document.body.append(document.createElement('button'));
document.querySelector('textarea').value = `
underscore_case
first_name
Some_Variable
calculate_AGE
delayed_departure
`

document.querySelector('button').addEventListener('click', function () {
    const text = document.querySelector('textarea').value;
    const rows = text.split('\n');
    let validrow = 0;
    for (const row of rows) {
        // 跳过空行
        const trimmedRow = row.trim()
        if (!trimmedRow) continue

        validrow++
        const [first, second] = row.toLowerCase().trim().split('_')
        const str = first + second.replace(second[0], second[0].toUpperCase())
        // padEnd 只传一个参数会在文本后填空格到指定位置
        console.log(`${str.padEnd(20)}${'✅'.repeat(validrow)}`)
    }
})