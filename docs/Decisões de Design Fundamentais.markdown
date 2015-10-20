# Decisões de Design Fundamentais


O sistema web da organização Atsia baseia-se num design do tipo Modelo-Visão-Controlador. Neste sistema é importante existir a separação da representação da informação da interacção que o Utilizador tem com a mesma. 
Como métodos de segurança existirá um sistema de Log-in que apenas permite o uso do Fórum por Utilizadores autenticados, sendo o processo de distribuição de credenciais de acesso efectuado pelo administrador do sistema garantindo acesso apenas às pessoas que participaram nos workshops. Isto permitirá o bloqueio de acesso a páginas não autorizadas por utilizadores não credenciados. Implementaremos também os protocolos de segurança (ex: SSL Certificate) e encriptação dos dados presentes na base de dados.