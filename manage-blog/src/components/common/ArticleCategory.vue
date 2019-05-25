<template>
    <el-select clearable v-model="id_copy" @change="value_change" filterable v-loading="loading" placeholder="请选择类别">
        <el-option
            v-for="item in lists"
            :label="item.name"
            :value="item.id">
        </el-option>
    </el-select>
</template>
<script>
    export default {
        data: function () {
            return {
                id_copy: "",
                lists: [],
                loading: false
            }
        },
        props: {
            id: {
                type: Number
            },
            major_id: {
                type: Number
            }
        },
        watch: {
            id: function (now) {
                if (now) {
                    this.id_copy = now
                }
            },
            major_id: function () {
                this.get_lists()
            }
        },
        methods: {
            get_lists: function () {
                this.loading = true
                this.$http.get("/paper/class", {params: {
                    major_id: this.major_id
                }}).then(function (response) {
                    this.loading = false
                    this.lists = response.data.class
                })
            },
            value_change: function () {
                let value = this.id_copy

                if (!value) {
                    this.$emit("change", null)
                    return
                }
                let lists = this.lists
                for (let i = 0; i < lists.length; i++) {
                    if (lists[i].id == value) {
                        this.$emit("change", lists[i])
                        break
                    }
                }
            }
        },
        mounted: function () {
            this.get_lists()
            if (this.id) {
                this.id_copy = this.id
            }
        }
    }
</script>