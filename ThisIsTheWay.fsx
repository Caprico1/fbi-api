#r "nuget: FSharp.Data"

open FSharp.Data

[<Literal>]
let sample = "https://api.fbi.gov/wanted/v1/list"
let apiUrl = "https://api.fbi.gov/wanted/v1/list"

type Wanted = JsonProvider<sample>

let wanted = Wanted.Load(apiUrl)
wanted.Items
|> Seq.iter(fun item ->
    printfn "%s" item.Title
)