console.log(forecasted_data);


const ctx = document.getElementById('weatherChart');

const labels = ["2016-12-25", "M", "2016-12-26", "M", "J", "J", "A"];
const data = {
    datasets: [
        {
            label: 'Real temperature',
            data: real_data,
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.5
        },
        {
            label: 'Forecasted temperature',
            data: forecasted_data,
            borderColor: 'rgb(192,75,75)',
            tension: 0.2
        },
    ]
};

const config = {
    type: 'line',
    data: data,
    options: {
        parsing: {
            xAxisKey: 'date',
            yAxisKey: 'temp'
        }
    }
};

new Chart(ctx, config);