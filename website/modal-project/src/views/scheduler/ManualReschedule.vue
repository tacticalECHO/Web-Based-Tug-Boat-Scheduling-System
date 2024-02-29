<template>
    <div id="ManualReschedule">
        <SideBar />
        <div class="pages">
            <router-view />
            <h2>{{id}}</h2>
            <table>
                <tr>
                    <td><b><label for="captain">Captain</label></b></td>
                    <td><select name="captain">
                            <option value="">John Smith</option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <td><b><label for="berth">Berth</label></b></td>
                    <td><select name="berth">
                            <option value="">John Smith</option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <td><b><label for="tugboat">Tug Boat</label></b></td>
                    <td><select name="tugboat">
                            <option value="">John Smith</option>
                        </select>
                    </td>
                </tr>
            </table>
        </div>
        <div class="cancel-save-buttons">
            <button class="grey-border-button" id="cancel" @click="redirect('Exit-ManualReschedule')">Cancel</button>
            <button class="blue-button" id="save" @click="save()">Save</button>
        </div>
    </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';

export default {
    name: 'ManualReschedule',
    components: {SideBar},
    data(){
        return{
            id: '',
        }
    },
    mounted() {
        // this.id = this.$route.query.id;
    },
    methods: {
        save(){
            //save pasword
            this.$router.push({name: 'Save-ManualReschedule'});
        }
    }
}
</script>

<style scoped>
table {
    text-align: left;
    font-size: 16;
    margin-bottom: 15px;
}

th, td {
    padding: 10px;
}

td {
    width: 150px;
}

select {
    border-radius: 5px;
    padding: 5px;
    width: 200px;
}
</style>
