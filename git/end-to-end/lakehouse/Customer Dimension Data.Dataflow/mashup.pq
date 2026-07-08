[DefaultOutputDestinationSettings = [DestinationDefinition = [Kind = "Reference", QueryName = "DefaultDestination", IsNewTarget = true], UpdateMethod = [Kind = "Replace"], DestinationTypeSettings = [Kind = "Table"]], StagingDefinition = [Kind = "FastCopy"]]
section Section1;
shared DefaultDestination = Lakehouse.Contents([EnableFolding = false]){[workspaceId = "292b5ad3-c5c5-454d-bf5d-c36fafdec4af"]}[Data]{[lakehouseId = "bbfdb079-1edb-4bb9-9888-ea1ae958a6d1"]}[Data];
[BindToDefaultDestination = true]
shared dimension_customer = let
  Source = Csv.Document(Web.Contents("https://raw.githubusercontent.com/microsoft/fabric-samples/refs/heads/main/docs-samples/data-engineering/dimension_customer.csv"), [Delimiter = ",", Columns = 11, Encoding = 65001, QuoteStyle = QuoteStyle.None]),
  #"Promoted headers" = Table.PromoteHeaders(Source, [PromoteAllScalars = true]),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"CustomerKey", Int64.Type}, {"WWICustomerID", Int64.Type}, {"Customer", type text}, {"BillToCustomer", type text}, {"Category", type text}, {"BuyingGroup", type text}, {"PrimaryContact", type text}, {"PostalCode", type text}, {"ValidFrom", type datetime}, {"ValidTo", type datetime}, {"LineageKey", Int64.Type}})
in
  #"Changed column type";
