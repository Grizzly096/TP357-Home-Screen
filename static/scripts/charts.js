const chartData = {
    labels: ["Normal", "Warnung", "Gefährlich"],
    data:[33.3,33.3,33.3],
    backgroundColor: [
        '#187327',
        '#fcb603',
        '#9c191f'
    ],
    offset:[20,20,20], 
    borderWidth: 0
}

const createGauge = (ctx) => {
    return new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: chartData.labels,
            datasets: [chartData]
        },
        options: {
            plugins: {
                legend: {
                    display: false
                },                
            },
            events: [],
            centerValue: "Lesen...",
            cutout: '75%', 
            rotation: -90,
            circumference: 180
        },
        plugins: [centerTextPlugin]
    });
}

const centerTextPlugin = {
    id: 'centerText',
    afterDraw(chart, args, options) {
        const { ctx, chartArea: { left, right, top, bottom } } = chart;
        ctx.save();

        const centerX = (left + right) / 2;
        const centerY = (top + bottom) / 2;

        console.log(left, right, top, bottom)

        ctx.font = '24px sans-serif';
        ctx.textAlign = "center";
        ctx.fillStyle = '#666666';
        ctx.fillText(chart.options.centerValue, centerX, centerY + 20);

        ctx.restore();
    }
};

const setGaugeValue = (chart, value, offset) => {
    chart.data.datasets[0].offset = offset;
    chart.options.centerValue = value;
    chart.update();
}