## STYLED COMPONENTS

Styled components are a CSS-in-JS tool that bridges the gap between components and styling, 
 offering numerous features to get you up and running in styling components in a functional 
  and reusable way. 




    import styled from "styled-components";

    // Styled component named StyledButton
    const StyledButton = styled.button`
    background-color: black;
    font-size: 32px;
    color: white;
    `;

    function Component() {
    // Use it like any other component.
    return <StyledButton> Login </StyledButton>;
    }



### Props

Allows styling of react components dynamically 
Let’s assume we have two types of buttons on our page, one 
 with a black background, and the other blue. We do not have 
  to create two styled components for them; we can adapt their styling based on their props. 


    import styled from "styled-components";

    const StyledButton = styled.button`
    min-width: 200px;
    border: none;
    font-size: 18px;
    padding: 7px 10px;
    /* The resulting background color will be based on the bg props. */
    background-color: ${props => {
        if(porps.bg==="black"){
            return "black"
        }
        if(porps.bg==="blue"){
            return "blue"
        }



    }
    
    ;
    `;

    function Profile() {
    return (
        <div>
        <StyledButton bg="black" type="button">Button A</StyledButton>
        <StyledButton bg="blue"type="button">Button B</StyledButton>
        </div>
    )
    }

### Extending styles

        
        const StyledContainer = styled.section`
        max-width: 1024px;
        padding: 0 20px;
        margin: 0 auto;
        `;

        // Inherit StyledContainer in StyledSmallConatiner
        const StyledSmallContainer = styled(StyledContainer)`
        padding: 0 10px;
        `;

        function Home() {
        return (
            <StyledContainer>
            <h1>The secret is to be happy</h1>
            </StyledContainer>
        );
        }

        function Contact() {
        return (
            <StyledSmallContainer>
            <h1>The road goes on and on</h1>
            </StyledSmallContainer>
        );
        }  


Alternatively we can use the as prop 
 
            function Home() {
        return (
            <StyledContainer>
            <h1>It’s business, not personal</h1>
            </StyledContainer>
        );
        }

        function Contact() {
        return (
            <StyledSmallContainer as={StyledContainer}>
            <h1>Never dribble when you can pass</h1>
            </StyledSmallContainer>
        );
        }



