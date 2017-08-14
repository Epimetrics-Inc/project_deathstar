## AO Serialization / Deserialization Notes

1. Use iconv to convert all files to ascii from utf-8

```
iconv -f utf-8 -t ascii//translit
```

2. Add opening and closing <data> tags to the whole file

3. Extract text from each of the elements, recursively.

4. Store to Postgres
