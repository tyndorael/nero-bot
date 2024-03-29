module.exports = {
  name: 'args-info',
  args: true,
  usage: '<user> <role>',
  description: 'Information about the arguments provided.',
  execute(message, args) {
    if (args[0] === 'foo') {
      return message.channel.send('bar');
    }

    return message.channel.send(
      `Arguments: ${args}\nArguments length: ${args.length}`,
    );
  },
};
