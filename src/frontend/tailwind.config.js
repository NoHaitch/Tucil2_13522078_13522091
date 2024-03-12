/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        transparent: 'transparent',
        current: 'currentColor',
        'bg1': '#1E1E1E',
        'bright-red1': '#FE1054',
        'bright-red2': '#b81846',
        'bright-blue': '#32BBF9',
        'bright-green': '#26F8B5',
      },
    },
  },
  plugins: [],
}