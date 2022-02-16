{
    "title": "Inventory",
    "date": "2022-02-16T18:45:18.881635+00:00",
    "draft": false
}

## pyhugodoc.inventory.InventoryItem
Inventory item.



#### \_\_init\_\_ _(special)_
**Signature**: ```__init__(self, name: str, domain: str, role: str, uri: str, priority: str = '1', dispname: Optional[str] = None) ```

Initialize the object.

**Parameters:**
- name  _(str)_: The item name.
- domain  _(str)_: The item domain, like 'python' or 'crystal'.
- role  _(str)_: The item role, like 'class' or 'method'.
- uri  _(str)_: The item URI.
- priority  _(str)_: The item priority. It can help for inventory suggestions.
- dispname  _(Optional[str])_: The item display name.





#### format\_sphinx
**Signature**: ```format_sphinx(self) -> str```

Format this item as a Sphinx inventory line.

**Returns:**
- str: A line formatted for an `objects.inv` file.



#### parse\_sphinx _(classmethod)_
**Signature**: ```parse_sphinx(line: str) -> InventoryItem```

Parse a line from a Sphinx v2 inventory file and return an `InventoryItem` from it.





#### sphinx\_item\_regex




## pyhugodoc.inventory.Inventory
Inventory of collected and rendered objects.



#### \_\_init\_\_ _(special)_
**Signature**: ```__init__(self, items: Optional[List[pyhugodoc.inventory.InventoryItem]] = None, project: str = 'project', version: str = '0.0.0') ```

Initialize the object.

**Parameters:**
- items  _(Optional[List[pyhugodoc.inventory.InventoryItem]])_: A list of items.
- project  _(str)_: The project name.
- version  _(str)_: The project version.





#### format\_sphinx
**Signature**: ```format_sphinx(self) -> bytes```

Format this inventory as a Sphinx `objects.inv` file.

**Returns:**
- bytes: The inventory as bytes.



#### parse\_sphinx _(classmethod)_
**Signature**: ```parse_sphinx(in_file: BinaryIO, *, domain_filter: Collection[str] = ()) -> Inventory```

Parse a Sphinx v2 inventory file and return an `Inventory` from it.

**Parameters:**
- in_file  _(BinaryIO)_: The binary file-like object to read from.
- domain_filter  _(Collection[str])_: A collection of domain values to allow (and filter out all other ones).

**Returns:**
- Inventory: An `Inventory` containing the collected `InventoryItem`s.



#### register
**Signature**: ```register(self, args, kwargs) ```

Create and register an item.

**Parameters:**
- *args : Arguments passed to [InventoryItem][mkdocstrings.inventory.InventoryItem].
- **kwargs : Keyword arguments passed to [InventoryItem][mkdocstrings.inventory.InventoryItem].
