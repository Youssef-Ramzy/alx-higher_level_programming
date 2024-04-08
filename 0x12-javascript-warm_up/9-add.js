#!/usr/bin/node
function add(a, b)
{
    const numA = Number(a);
    const numB = Number(b);
    if (isNaN(numA) || isNaN(numB))
    {
        console.log('Missing size');
        return;
    }
    const result = numA + numB;
    console.log(result);
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

add(arg1, arg2);