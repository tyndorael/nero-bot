module.exports = {
  name: 'padoru',
  description: 'Padoru!',
  cooldown: 5,
  execute(message) {
    return message.channel.send('https://www.youtube.com/watch?v=MUpAtUuNG2A');
  },
};
