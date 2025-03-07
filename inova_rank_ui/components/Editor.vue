<template>
    <div class="border rounded-md ">
        <div v-if="editor" class="flex gap-2 bg-emerald-200 dark:bg-slate-700 p-2 rounded-md">
            <UButton :variant="showHeadings ? 'soft' : 'ghost'" @click="showHeadings = !showHeadings">
                <UIcon name="i-tabler-heading" class="w-5 h-5" />
            </UButton>
            <div v-if="showHeadings" class="toggle-list">
                <UButton variant="ghost" @click="editor.chain().focus().toggleHeading({ level: 1 }).run()"
                    :class="{ 'is-active': editor.isActive('heading', { level: 1 }) }">
                    <UIcon name="i-tabler-h-1" class="w-5 h-5" />
                </UButton>
                <UButton variant="ghost" @click="editor.chain().focus().toggleHeading({ level: 2 }).run()"
                    :class="{ 'is-active': editor.isActive('heading', { level: 2 }) }">
                    <UIcon name="i-tabler-h-2" class="w-5 h-5" />
                </UButton>
                <UButton variant="ghost" @click="editor.chain().focus().toggleHeading({ level: 3 }).run()"
                    :class="{ 'is-active': editor.isActive('heading', { level: 3 }) }">
                    <UIcon name="i-tabler-h-3" class="w-5 h-5" />
                </UButton>
                <UButton variant="ghost" @click="editor.chain().focus().toggleHeading({ level: 4 }).run()"
                    :class="{ 'is-active': editor.isActive('heading', { level: 4 }) }">
                    <UIcon name="i-tabler-h-4" class="w-5 h-5" />
                </UButton>
                <UButton variant="ghost" @click="editor.chain().focus().toggleHeading({ level: 5 }).run()"
                    :class="{ 'is-active': editor.isActive('heading', { level: 5 }) }">
                    <UIcon name="i-tabler-h-5" class="w-5 h-5" />
                </UButton>
                <UButton variant="ghost" @click="editor.chain().focus().toggleHeading({ level: 6 }).run()"
                    :class="{ 'is-active': editor.isActive('heading', { level: 6 }) }">
                    <UIcon name="i-tabler-h-6" class="w-5 h-5" />
                </UButton>
            </div>
            <UButton :variant="editor.isActive('bold') ? 'soft' : 'ghost'"
                @click="editor.chain().focus().toggleBold().run()"
                :disabled="!editor.can().chain().focus().toggleBold().run()"
                :class="{ 'is-active': editor.isActive('bold') }">
                <UIcon :name="editor.isActive('bold') ? 'i-tabler-bold' : 'i-tabler-bold-off'" class="w-5 h-5" />
            </UButton>
            <UButton :variant="editor.isActive('italic') ? 'soft' : 'ghost'"
                @click="editor.chain().focus().toggleItalic().run()"
                :disabled="!editor.can().chain().focus().toggleItalic().run()"
                :class="{ 'is-active': editor.isActive('italic') }">
                <UIcon name="i-tabler-italic" class="w-5 h-5" />
            </UButton>
            <UButton :variant="editor.isActive('strike') ? 'soft' : 'ghost'"
                @click="editor.chain().focus().toggleStrike().run()"
                :disabled="!editor.can().chain().focus().toggleStrike().run()"
                :class="{ 'is-active': editor.isActive('strike') }">
                <UIcon name="i-tabler-strikethrough" class="w-5 h-5" />
            </UButton>
            <UButton :variant="editor.isActive('code') ? 'soft' : 'ghost'"
                @click="editor.chain().focus().toggleCode().run()"
                :disabled="!editor.can().chain().focus().toggleCode().run()"
                :class="{ 'is-active': editor.isActive('code') }">
                <UIcon name="i-tabler-code" class="w-5 h-5" />
            </UButton>
            <UButton :variant="editor.isActive('code') ? 'soft' : 'ghost'"
                @click="editor.chain().focus().toggleCodeBlock().run()"
                :class="{ 'is-active': editor.isActive('codeBlock') }">
                <UIcon name="i-tabler-code-dots" class="w-5 h-5" />
            </UButton>
            <UButton :variant="editor.isActive('bulletList') ? 'soft' : 'ghost'"
                @click="editor.chain().focus().toggleBulletList().run()"
                :class="{ 'is-active': editor.isActive('bulletList') }">
                <UIcon name="i-tabler-list" class="w-5 h-5" />
            </UButton>
            <UButton :variant="editor.isActive('orderedList') ? 'soft' : 'ghost'"
                @click="editor.chain().focus().toggleOrderedList().run()"
                :class="{ 'is-active': editor.isActive('orderedList') }">
                <UIcon name="i-tabler-list-numbers" class="w-5 h-5" />
            </UButton>
            <UButton :variant="editor.isActive('blockquote') ? 'soft' : 'ghost'"
                @click="editor.chain().focus().toggleBlockquote().run()"
                :class="{ 'is-active': editor.isActive('blockquote') }">
                <UIcon name="i-tabler-blockquote" class="w-5 h-5" />
            </UButton>
            <UButton variant="soft" @click="editor.chain().focus().setHorizontalRule().run()">
                <UIcon name="i-tabler-separator" class="w-5 h-5" />
            </UButton>
            <UButton variant="soft" @click="editor.chain().focus().setHardBreak().run()">
                <UIcon name="i-tabler-baseline-density-large" class="w-5 h-5" />
            </UButton>
            <UButton variant="soft" @click="editor.chain().focus().unsetAllMarks().run()">
                <UIcon name="i-tabler-clear-formatting" class="w-5 h-5" />
            </UButton>
            <UButton :variant="editor.can().chain().focus().undo().run() ? 'soft' : 'ghost'"
                @click="editor.chain().focus().undo().run()" :disabled="!editor.can().chain().focus().undo().run()">
                <UIcon name="i-tabler-corner-up-left-double" class="w-5 h-5" />
            </UButton>
            <UButton :variant="editor.can().chain().focus().redo().run() ? 'soft' : 'ghost'"
                @click="editor.chain().focus().redo().run()" :disabled="!editor.can().chain().focus().redo().run()">
                <UIcon name="i-tabler-corner-up-right-double" class="w-5 h-5" />
            </UButton>
        </div>
        <TiptapEditorContent :editor="editor"
            class="w-full rounded-md p-4 leading-tight focus:outline-none focus:shadow-outline bg-transparent" />
    </div>
</template>

<script setup>
import { ref } from "vue";
import BulletList from "@tiptap/extension-bullet-list";
import OrderedList from "@tiptap/extension-ordered-list";
import Heading from "@tiptap/extension-heading";
import CodeBlock from "@tiptap/extension-code-block";

const showHeadings = ref(false);
const editor = useEditor({
    content: "<p>Desenvolva sua ideia aqui</p>",
    extensions: [
        TiptapStarterKit,
        BulletList,
        OrderedList,
        Heading.configure({
            levels: [1, 2, 3, 4, 5, 6],
        }),
        CodeBlock.configure({
            defaultLanguage: "js",
            exitOnTripleEnter: false,
        }),
    ],
});

onBeforeUnmount(() => {
    unref(editor).destroy();
});
</script>

<style lang="css">
/* Basic editor styles */
.tiptap {
    outline: none;

    :first-child {
        margin-top: 0;

        :focus-visible {
            outline: none;
        }
    }

    /* List styles */
    ul,
    ol {
        padding: 0 1rem;
        margin: 1.25rem 1rem 1.25rem 0.4rem;

        li p {
            margin-top: 0.25em;
            margin-bottom: 0.25em;
            list-style-type: inherit;
            list-style-position: inherit;
            padding-left: 0.5rem;
        }

        list-style-type: disc;
                
    }

    ol {
        list-style-type: decimal;
    }

    /* Heading styles */
    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        line-height: 1.1;
        margin-top: 2.5rem;
        text-wrap: pretty;
    }

    h1,
    h2 {
        margin-top: 3.5rem;
        margin-bottom: 1.5rem;
    }

    h1 {
        font-size: 2rem;
    }

    h2 {
        font-size: 1.8rem;
    }

    h3 {
        font-size: 1.6rem;
    }

    h4 {
        font-size: 1.4rem;
    }

    h5 {
        font-size: 1.2rem;
    }

    h6 {
        font-size: 1rem;
    }

    pre {
        background: rgb(215, 255, 225);
        border-radius: 0.5rem;
        border-color: rgb(144, 255, 172);
        color: rgb(24, 99, 43);
        font-family: "JetBrainsMono", monospace;
        margin: 1.5rem 0;
        padding: 0.75rem 1rem;

        code {
            background: none;
            color: inherit;
            font-size: 0.8rem;
            padding: 0;
        }
    }
}
</style>
