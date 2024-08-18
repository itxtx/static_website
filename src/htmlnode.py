class HTMLNode:
    
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.props = props #or {}
        self.children = children #or []
        
    def to_html(self):
        raise NotImplementedError()
        if self.tag is None:
            return self.value or ""
        children_html = "".join([child.to_html() for child in self.children])
        props_html = self.props_to_html()
        if self.value:
            return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"

        
    def props_to_html(self):
        if not self.props:
            return ''
        return "".join([f' {key}="{value}"' for key, value in self.props.items()])
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
    

    
    
    
class LeafNode(HTMLNode):
        
    def __init__(self, tag, value,props=None):
        if value is None:
            raise ValueError("LeafNode must have a value.")
        super().__init__(tag,value,None,props=props)
        
    def to_html(self):
        if self.tag is None:
            return self.value  # Return raw text if there is no tag
        else:
            props_html = self.props_to_html()
            if props_html:
                return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            
            
            
            

class ParentNode(HTMLNode):
    def __init__(self,  tag, children, props=None):
        if children is None:
            raise ValueError("ParentNode must have a child.")
        super().__init__(tag, None, children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag.")
        if self.children is None:
            raise ValueError("ParentNode must have a child.")
        
        children_html = "".join([child.to_html() for child in self.children])   #!!!!
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

        
        
        
        


