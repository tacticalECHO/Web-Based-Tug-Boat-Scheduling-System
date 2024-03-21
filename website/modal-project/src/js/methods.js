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
    let color;

    switch (state) {
        case 'Confirmed':
            backgroundColor = 'rgb(52, 144, 186)';
            color = 'white';
            break;
        case 'Free':
            backgroundColor = 'rgb(0, 255, 0, 0.2)';
            color = 'darkgreen';
            break;
        case 'Scheduled':
            backgroundColor = 'rgb(254, 219, 46)';
            color = 'white';
            break;
        case 'Busy':
            backgroundColor = 'rgb(255,0,0,0.2)';
            color = 'darkred';
            break;
        case 'Completed':
            backgroundColor = 'darkgrey';
            color = 'white';
            break;
        case 'Maintenance':
            backgroundColor = 'rgb(211,211,211,0.2)';
            color = 'darkgrey';
            break;
        default:
            backgroundColor = 'lightgrey';
            color = 'white';
    }

    switch (type) {
        case 'Completed':
            backgroundColor = 'rgb(213, 212, 212)';
            color = 'white';
            break;
        default:
            backgroundColor = backgroundColor;
    }

    return {
        background: backgroundColor,
        color: color,
    };
}

export function getActionStyle(action, type){
    let backgroundColor;
    let color;

    switch (action) {
        case 'INBOUND':
            backgroundColor = 'rgb(151, 214, 135, 0.5)';
            color = 'darkgreen';
            break;
        case 'OUTBOUND':
            backgroundColor = 'rgb(237, 237, 149, 0.5)';
            color = 'rgb(128, 114, 9)';
            break;
    }

    switch (type) {
        case 'Completed':
            backgroundColor = 'rgb(213, 212, 212)';
            color = 'white';
            break;
        default :
            backgroundColor = backgroundColor;
    }
    return {
        background: backgroundColor,
        color : color,
    };
}

export function toggle() {
    this.resetNull();
}

export function getCaptainId(id){
    const tugboat = this.tugboats.find((tugboat) => tugboat.TugBoatId === id);
    return tugboat && tugboat.CaptainId ? tugboat.CaptainId.CaptainId : "-";
}

export function getCaptainName(id){
    const tugboat = this.tugboats.find((tugboat) => tugboat.TugBoatId === id);
    return tugboat && tugboat.CaptainId ? tugboat.CaptainId.name : "-";
}

export function deletionAlert(){
    const deletion = confirm("Confirm to delete?");
    return deletion
}