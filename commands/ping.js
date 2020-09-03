module.exports = {
  name: 'ping',
  description: 'Ping!',
  cooldown: 5, // seconds
  execute(message) {
    return message.channel.send('Pong.');
  },
};
