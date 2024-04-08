#!/usr/bin/node
const args = process.argv.slice(2).map(Number);

if (args.length < 2)
    console.log(0);
else
{
    let largest = -Infinity
    let secondLargest = -Infinity

    for (let i = 0; i < args.length; i++)
    {
        if (args[i] > largest)
        {
            secondLargest = largest;
            largest = args[i];
        }
        else if (args[i] > secondLargest && args[i] < largest)
        {
            secondLargest = args[i];
        }
    }
    console.log(secondLargest !== -Infinity ? secondLargest : 0);
}