<template>
    <div class="backdrop">
        <div class="container-position">
            <div class="popup-container">
                <table>
                    <tr>
                        <td>/</td>
                        <td><b>Sucessful</b><br/>upload the task list succesfully.</td>
                        <td><button>Confirm</button></td>
                    </tr>
                </table>  
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Successful',
    props: [],
}
</script>

<style scoped>
.backdrop{
    background: none;
}
.container-position {
    margin-top: 20px;
}
.popup-container {
    width: 400px;
}
</style>
