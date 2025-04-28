'use strict';

const data = [
    [17, 21, 23],
    [12, 5, -5, 0, 4],
];

const printForecast = (arr) => {
    let result = '... ';
    result += arr
        .map((temp, index) => `${temp}ºC in ${index + 1} days ...`)
        .join(' ');
    console.log(result);
};

printForecast(data[0]);