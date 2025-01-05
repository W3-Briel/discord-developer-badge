# Bot de Discord en Python

Este es un bot simple hecho en Python que cumple con los requisitos para obtener la insignia de Desarrollador Activo en Discord.

## Instrucciones

### 1. Crear una Aplicación en Discord
- Ve a [Discord Developers](https://discord.com/developers/applications).
- Selecciona tu bot y ve al apartado de **OAuth2**.

### 2. Configurar el Bot
- En **OAuth2 URL Generator**, selecciona la opción **bot**.
- Desplázate hacia abajo y selecciona **Administrador**.
- Copia el enlace que aparece y añádelo a un servidor de Discord.

### 3. Obtener y Configurar el Token
- En el apartado **Bot**, haz clic en el botón **Reset Token** para obtener un nuevo token.
- Copia el token y pégalo en el archivo de tu proyecto, asignándolo a `DISCORD_BOT_SECRET_TOKEN`.
- En el mismo apartado, activa las siguientes opciones bajo **Privileged Gateway Intents**:
  - **MESSAGE CONTENT INTENT**
  - **PRESENCE INTENT**

### 4. Ejecutar el Bot
- Ejecuta tu código.
- Una vez que el bot esté conectado, utiliza el comando `/insignia` en Discord.

### 5. Reclamar la Insignia
- Solo queda esperar unos días y reclamar la insignia en [Discord Active Developer](https://discord.com/developers/active-developer).

¡Listo! Ahora tienes un bot funcional que te ayudará a obtener la insignia de Desarrollador Activo en Discord.
