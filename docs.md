## Prompt Templating

Prompt templating allows you to define templates in Semantic Kernel that can be filled with parameters to generate responses. These templates act as prompts that the AI agent can use to gather more context or request additional information from the user.

For example, you may have a template called "Greetings" that says "Hello! My name is {agent name}. How can I help you today?". When this template is executed, it will fill in the {agent name} parameter with the actual name of the AI agent.

Templates are defined using a simple JSON format. Each template has a unique name that is used to reference it. It also contains the text of the template which can include parameter placeholders wrapped in curly braces.

Here is a simple .NET example:

csharp

Insert at cursor

Copy
// Define a prompt template
PromptTemplate greetingsTemplate = new PromptTemplate()
{
  Name = "Greetings",
  Text = "Hello! My name is {agent_name}. How can I help you today?" 
};

// Add the template to the kernel
kernel.AddTemplate(greetingsTemplate);

// Execute the template, passing values for the parameters  
string response = await kernel.ExecuteTemplateAsync(
  "Greetings", 
  new { agent_name = "Amazon Q" });

Console.WriteLine(response); 
// Prints "Hello! My name is Amazon Q. How can I help you today?"
Templates allow you to define reusable question/response patterns that can be filled dynamically based on the context of the conversation. The agent can choose an appropriate template to use based on its state and goals.