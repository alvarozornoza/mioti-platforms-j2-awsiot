let humArr = [], tempArr = [], upArr = [];
let myChart = Highcharts.chart('container1', {

    title: {
        text: 'Title'
    },

    yAxis: {
        title: {
            text: 'Value'
        }
    },

    xAxis: {
        categories: upArr,
        labels:{
            formatter:function(){
                return Highcharts.dateFormat('%H:%M:%S',this.value);
            }
         }
    },

    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },

    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            }
        }
    },
    series: [{
        name: 'Humedad',
        data: []
    }, {
        name: 'Temperatura',
        data: []
    }],

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }
});

let getTelemetryData = function () {
    $.ajax({
        type: "GET",
        url: "https://alvaro-bucket-01.s3.eu-west-3.amazonaws.com/alvaro-device-01",  //example: https://mydatabucket.s3.amazonaws.com/myKey"
        dataType: "json",
        async: false,
        success: function (data) {
            drawChart(data);
        },
        error: function (xhr, status, error) {
            console.error("JSON error: " + status);
        }
    });
}

let drawChart = function (data) {

    let humidity = data.humidity;
    let temperature = data.temperature;
    let timestamp = data.timestamp;

    humArr.push(Number(humidity));
    tempArr.push(Number(temperature));
    upArr.push(Number(timestamp));

    myChart.series[0].setData(humArr , true)
    myChart.series[1].setData(tempArr , true)
}

let intervalTime = 3 * 1000; // 3 second interval polling, change as you like
setInterval(() => {
    getTelemetryData();
}, intervalTime);