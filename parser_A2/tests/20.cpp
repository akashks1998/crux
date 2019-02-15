

class PrintFunctionsConsumer : public ASTConsumer
{
  CompilerInstance &Instance;
  set<|string|> ParsedTemplates;

public:


  void HandleTranslationUnit(ASTContext &context)
  {

    struct Visitor : public RecursiveASTVisitor<|Visitor|>
    {
      const set<|string|> &ParsedTemplates;
    };
  }
};
