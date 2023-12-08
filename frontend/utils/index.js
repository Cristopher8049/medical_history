const { useMultiFileAuthState, makeWASocket, DisconnectReason } = require("@whiskeysockets/baileys");

const log = (pino = require("pino"));
const { session } = { session: "session_auth_info" };
const { Boom } = require("@hapi/boom");
const express = require("express");
const fileUpload = require("express-fileupload");
const cors = require("cors");
const bodyParser = require("body-parser");
const app = require("express")();
app.use(
  fileUpload({
    createParentPath: true,
  })
);

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
const server = require("http").createServer(app);
const io = require("socket.io")(server);
const port = process.env.PORT || 8000;
const qrcode = require("qrcode");

app.get("/qr", async (req, res) => {
   if (!qrDinamic) {
      return res.status(400).json({ error: "No hay código QR disponible." });
    }

    const qrCodeDataURL = await qrcode.toDataURL(qrDinamic);

    res.status(200).json({ qrCodeURL: qrCodeDataURL });
})
  
app.get("/connect", async (req, res) => {
  try {
    await connectToWhatsApp();

    const checkQR = () => {
      if (!qrDinamic) {
        setTimeout(checkQR, 0); 
      } else {
        const qrCodeDataURL = qrcode.toDataURL(qrDinamic, (err, url) => {
          if (err) {
            console.error('Error al generar el código QR:', err);
            res.status(500).json({ error: 'Error al generar el código QR' });
          } else {
            res.status(200).json({ qrCodeURL: url });
          }
        });
      }
    };

    checkQR();
  } catch (error) {
    console.error('Error al conectar a WhatsApp:', error);
    res.status(500).json({ error: 'Error al conectar a WhatsApp' });
  }
});




app.get("/", (req, res) => {
  res.send("server working");
});

let sock;
let qrDinamic;
let soket;

async function connectToWhatsApp() {
  const { state, saveCreds } = await useMultiFileAuthState("session_auth_info");

  sock = makeWASocket({
    printQRInTerminal: true,
    auth: state,
    logger: log({ level: "silent" }),
  });

  sock.ev.on("connection.update", async (update) => {
    const { connection, lastDisconnect, qr } = update;
    qrDinamic = qr;
  
    if (connection === "close") {
      let reason = new Boom(lastDisconnect.error).output.statusCode;
      if (reason === DisconnectReason.badSession) {
        console.log(
          `Bad Session File, Please Delete ${session} and Scan Again`
        );
        sock.logout();
      } else if (reason === DisconnectReason.connectionClosed) {
        console.log("Conexión cerrada, reconectando....");
        connectToWhatsApp();
      } else if (reason === DisconnectReason.connectionLost) {
        console.log("Conexión perdida del servidor, reconectando...");
        connectToWhatsApp();
      } else if (reason === DisconnectReason.connectionReplaced) {
        console.log(
          "Conexión reemplazada, otra nueva sesión abierta, cierre la sesión actual primero"
        );
        sock.logout();
      } else if (reason === DisconnectReason.loggedOut) {
        console.log(
          `Dispositivo cerrado, elimínelo ${session} y escanear de nuevo.`
        );
        sock.logout();
      } else if (reason === DisconnectReason.restartRequired) {
        console.log("Se requiere reinicio, reiniciando...");
        connectToWhatsApp();
      } else if (reason === DisconnectReason.timedOut) {
        console.log("Se agotó el tiempo de conexión, conectando...");
        connectToWhatsApp();
      } else {
        sock.end(
          `Motivo de desconexión desconocido: ${reason}|${lastDisconnect.error}`
        );
      }
    } else if (connection === "open") {
      console.log("conexión abierta");
      return;
    }
  });

  sock.ev.on("creds.update", saveCreds);
}

io.on("connection", async (socket) => {
  soket = socket;
  soket?.emit("qr", url);

});


server.listen(port, () => {
  console.log("Server Run Port : " + port);
});
