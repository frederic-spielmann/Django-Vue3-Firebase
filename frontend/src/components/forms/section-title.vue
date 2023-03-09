<template>
    <div>
        <div>
            <h1 class="center">
                <slot name="title"></slot>
            </h1>

            <p>
                <slot name="description"></slot>
            </p>
        </div>

        <div class="">
            <slot name="aside"></slot>
        </div>
    </div>
</template>

<style>
.center {
  text-align: center;
}
</style>