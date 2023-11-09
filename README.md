# Arsitektur Mikroservis dengan gRPC

## Deskripsi Arsitektur

Proyek ini menggunakan arsitektur mikroservis untuk memecah aplikasi menjadi layanan yang lebih kecil dan terpisah. Setiap layanan fokus pada suatu fungsionalitas tertentu dan dapat berkomunikasi satu sama lain menggunakan protokol gRPC.

## Layanan

- **Layanan Produk**: Mengelola operasi terkait produk, seperti menambah, menghapus, atau mengubah informasi produk.
- **Layanan Pemesanan**: Bertanggung jawab atas proses pemesanan, perhitungan harga, dan pembayaran.
- **Layanan Pengguna**: Mengelola informasi pengguna, otentikasi, dan otorisasi.
- **Layanan Pengiriman**: Mengelola proses pengiriman, termasuk mengaktifkan, menonaktifkan, dan menambah/mengubah/menghapus layanan pengiriman.
- **Layanan Pembayaran**: Mengelola proses pembayaran, termasuk mengaktifkan, menonaktifkan, dan menambah/mengubah/menghapus layanan pembayaran.

## Komunikasi Antar Layanan

Layanan dalam sistem berkomunikasi satu sama lain menggunakan protokol gRPC. Protokol ini memungkinkan layanan untuk memanggil metode layanan lain seolah-olah metode tersebut adalah metode lokal. Hal ini mempermudah integrasi dan komunikasi antar layanan.

## Interaksi Antar Layanan dengan gRPC

gRPC adalah framework komunikasi antar layanan yang memungkinkan layanan untuk berkomunikasi satu sama lain melalui panggilan prosedur jarak jauh (RPC). Dalam arsitektur mikroservis ini, gRPC digunakan untuk menghubungkan layanan satu dengan lainnya.

Misalnya, ketika pengguna menambahkan produk ke keranjang belanja, layanan Pemesanan dapat memanggil layanan Produk untuk mendapatkan informasi produk yang terkait. Ini dilakukan dengan membuat panggilan RPC ke metode yang didefinisikan dalam layanan Produk.

Setiap layanan mendefinisikan antarmuka API mereka sendiri menggunakan bahasa definisi antarmuka (IDL) protobuf. Protobuf adalah format data ringan yang digunakan untuk serialisasi data antara layanan. Dengan menggunakan protobuf, gRPC dapat menghasilkan kode sumber untuk klien dan server dalam berbagai bahasa pemrograman, memudahkan integrasi antar layanan yang ditulis dalam bahasa yang berbeda.


# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
