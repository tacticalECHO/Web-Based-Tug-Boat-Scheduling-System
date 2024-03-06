export function redirect(event){
    this.$router.push({name: event});
}

export function formatTime(event){
    const dateTime = new Date(event);
    const hours = dateTime.getHours().toString().padStart(2, '0');
    const minutes = dateTime.getMinutes().toString().padStart(2, '0');

    return `${hours}:${minutes}`;
}

export function formatDate(event){
    const dateTime = new Date(event);
    const date = dateTime.getDate().toString().padStart(2, '0');
    const month = (dateTime.getMonth()+1).toString().padStart(2, '0');

    return `${date}/${month}`;
}

export function getStatusStyle(state, type){
    let backgroundColor;

    switch (state) {
        case 'Confirmed':
        backgroundColor = 'green';
        break;
        case 'Scheduled':
        backgroundColor = 'rgb(254, 219, 46)';
        break;
        case 'Completed':
        backgroundColor = 'darkgrey';
        break;
        default:
        backgroundColor = 'lightgrey';
    }

    switch (type) {
        case 'Completed':
            backgroundColor = 'rgb(213, 212, 212)';
            break;
        default:
            backgroundColor = backgroundColor;
    }

    return {
        background: backgroundColor,
    };
}

export function getActionStyle(action, type){
    let backgroundColor;

    switch (action) {
        case 'Arrival':
            backgroundColor = '#72bedf';
            break;
        default:
            backgroundColor = '#020071';
    }

    switch (type) {
        case 'Completed':
            backgroundColor = 'rgb(213, 212, 212)';
            break;
        default:
            backgroundColor = backgroundColor;
    }

    return {
        color: 'white',
        background: backgroundColor,
    };
}