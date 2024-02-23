<template>
    <div class="backdrop">
        <div class="container-position">
            <div class="popup-container">
                <button @click="close">X</button>
                <br/>
                <table>
                    <tr>
                        <td><button @click="details()">Yibai Yuan did not confirm</button></td>
                    </tr>
                    <tr>
                        <td><button>Yibai Yuan did not confirm</button></td>
                    </tr>
                    <tr>
                        <td><button>Yibai Yuan did not confirm</button></td>
                    </tr>
                    <tr>
                        <td><button>Yibai Yuan did not confirm</button></td>
                    </tr>
                </table>
                <br/> 
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Message',
    props: [],
    methods: {
        close(){
            this.$router.back();
        },
        details(){
            this.$router.push({name: 'MessageDetails'});
        }
    }
}
</script>

<style scoped>
button {
    width: 30px;
    height: 30px;
    border: none;
    font-size: 15px;
}

table button{
    width: 100%;
    height: 100%;
    font-size: var(--font-size);
    border-radius: none;
}

table button:hover{
    background: rgba(140, 187, 192, 0.5);
}

.popup-container {
    width: 700px;
    height: 430px;
}

.container-position {
    margin-top: 120px;
}

table {
    margin-left: 50px;
    margin-right: 50px;
    border-collapse: collapse;
    border-spacing: 0;
}

tr, td {
    border: 1px solid var(--main-button-color);
}

</style>
