const formatNumber = (value, affix = '') => {
    const number = Number(value);
    if (Number.isNaN(number)) {
        return '';
    }
    const [integerPart, fractionPart] = String(number).split('.');
    const formatted = fractionPart ? `${integerPart},${fractionPart}` : integerPart;
    return affix ? `${formatted} ${affix}` : formatted;
}

const updateDisplay = (data) => {
    const temperature = data.temperature;
    const humidity = data.humidity;

    let temperatureIndex = undefined;

    temperatureLimit.some((value, index) => {
        if (temperature <= value) {
        temperatureIndex = index;
        return true;
        }
    })

    let humidityIndex = undefined;

    humidityLimit.some((value, index) => {
        if (humidity <= value) {
        humidityIndex = index;
        return true;
        }
    })

    let temperatureOffset = [20, 20, 20];
    let humidityOffset = [20, 20, 20];

    temperatureOffset[temperatureIndex] = 70;
    humidityOffset[humidityIndex] = 70;
    
    console.log(temperature, humidity, temperatureOffset, humidityOffset)
    setGaugeValue(temperatureChart, formatNumber(temperature, "°C"), temperatureOffset);
    setGaugeValue(humidityChart, formatNumber(humidity, "%"), humidityOffset);
}

const sendAjax = (url, method, data = {}) => {
    return $.ajax({
        url: url,
        method: method,
        data: JSON.stringify(data)
    }).done((data) => {
        return data;
    }).error((data) => {
        return data
    })
}