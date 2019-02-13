

class PrintFunctionsConsumer : public ASTConsumer {
  CompilerInstance &Instance;
  std::set<std::string> ParsedTemplates;

public:
  PrintFunctionsConsumer(CompilerInstance &Instance,
                         std::set<std::string> ParsedTemplates)
      : Instance(Instance), ParsedTemplates(ParsedTemplates) {}

  void HandleTranslationUnit(ASTContext& context) override {

    struct Visitor : public RecursiveASTVisitor<Visitor> {
      const std::set<std::string> &ParsedTemplates;
    } v(ParsedTemplates);
    clang::Sema &sema = Instance.getSema();
    for (const FunctionDecl *FD : v.LateParsedDecls) {
      llvm::errs() << "late-parsed-decl: \"" << FD->getNameAsString() << "\"\n";
    }   
  }
};

