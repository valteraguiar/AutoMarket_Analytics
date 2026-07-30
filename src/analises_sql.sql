
-- =========================================
-- TOP 10 MARCAS POR PREÇO MÉDIO
-- =========================================

SELECT
    brand,
    ROUND(AVG(avg_price_brl), 2) AS preco_medio
FROM carros
GROUP BY brand
ORDER BY preco_medio DESC
LIMIT 10;


-- =========================================
-- TOP 10 MARCAS MAIS PRESENTES
-- =========================================

SELECT
    brand,
    COUNT(*) AS quantidade
FROM carros
GROUP BY brand
ORDER BY quantidade DESC
LIMIT 10;


-- =========================================
-- PREÇO MÉDIO POR COMBUSTÍVEL
-- =========================================

SELECT
    fuel,
    COUNT(*) AS quantidade,
    ROUND(AVG(avg_price_brl), 2) AS preco_medio
FROM carros
GROUP BY fuel
ORDER BY preco_medio DESC;


-- =========================================
-- PREÇO MÉDIO POR CÂMBIO
-- =========================================

SELECT
    gear,
    COUNT(*) AS quantidade,
    ROUND(AVG(avg_price_brl), 2) AS preco_medio
FROM carros
GROUP BY gear
ORDER BY preco_medio DESC;
