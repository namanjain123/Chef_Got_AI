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





code of quandrant

using Microsoft.SemanticKernel.Connectors.AI.OpenAI;
using Microsoft.SemanticKernel.Connectors.Memory.Qdrant;
using Microsoft.SemanticKernel.Memory;
using Microsoft.SemanticKernel.Plugins.Memory;

namespace HindalcoGPT.Qdrant
{
    public partial class Qdrant
    {
        //private  QdrantMemoryStore memoryStore;
        #region credential
        string URL = "";
        int SIZE = 1536;
        string AzureEndpoint = "";
        string ApiKey = "";
        #endregion
        private ISemanticTextMemory kernel;

        
        public Qdrant(string model="text-embedding-ada-002",string? url =null, int? size= null, 
            string? azure_endpoint = null, string? apikey = null)
        {
            URL = url ?? URL;
            SIZE = size ?? SIZE;
            AzureEndpoint = azure_endpoint ?? AzureEndpoint;
            ApiKey = apikey ?? ApiKey;

            //memoryStore= new(url, port);
            kernel = new MemoryBuilder()
                .WithAzureTextEmbeddingGenerationService
                (model,
               AzureEndpoint, // Azure OpenAI *Endpoint* 
               ApiKey // Azure OpenAI *Key*).
               ).WithQdrantMemoryStore(URL, SIZE)
               .Build();
        }

        /// <summary>
        /// Gets a group of all available collection names.
        /// </summary>
        /// <returns>A group of collection names.</returns>
        public async Task<IList<string>> GetCollection() => await kernel.GetCollectionsAsync();
        //public IAsyncEnumerable<string> GetCollection() => memoryStore.GetCollectionsAsync();
        
        /// <summary>
        /// Remove a memory by key.
        /// For local memories the key is the "id" used when saving the record.
        /// For external reference, the key is the "URI" used when saving the record.
        /// </summary>
        /// <param name="collection">Collection to search.</param>
        /// <param name="key">Unique memory record identifier.</param>
        public async Task DeleteCollection(string collection,string key) => await kernel.RemoveAsync(collection, key);

    }
}


using Microsoft.SemanticKernel.Memory;

namespace HindalcoGPT.Qdrant
{
    public partial class Qdrant
    {
        private const string
            requestCollection = ""
            , queryCollection = "";

        /// <summary>
        /// Check is similar request is been made previously or not 
        /// </summary>
        /// <param name="request"></param>
        /// <param name="threshold"></param>
        /// <returns>The appropriate SQL query</returns>
        public async Task<string> CheckSqlInQdrant(string request, float threshold = 0.945f)
        {
            try
            {
                var results = kernel.SearchAsync(requestCollection, request, limit: 1, minRelevanceScore: threshold);

                bool isEmpty = true;
                string sqlQuery = null;
                await foreach (var r in results)
                {
                    isEmpty = false;
                    string id = r.Metadata.Id;
                    //geting sql query 
                    MemoryQueryResult? lookup = await kernel.GetAsync(queryCollection, id);
                    sqlQuery = lookup.Metadata.Text;
                }
                if (isEmpty == true) return null;
                else return sqlQuery;
            }
            catch (Exception ex) { return null; }

        }

        /// <summary>
        /// Save the responce from the if Information is not  stored in VectorDB (ex. 'Qdrant')
        /// </summary>
        /// <param name="request">  </param>
        /// <param name="sql" ></param>
        public async Task SaveSqlInQdrant(string request, string sql_query)
        {
            try
            {
                string id = Guid.NewGuid().ToString();
                var x = await kernel.SaveInformationAsync(requestCollection, id: id, text: request);
                var y = await kernel.SaveInformationAsync(queryCollection, id: id, text: sql_query);
            }
            catch { }
        }
    }
}


