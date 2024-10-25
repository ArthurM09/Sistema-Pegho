import React, { useState } from 'react';
import api from '../api';
import DadosPessoaisForm from './DadosPessoaisForm';
import ContatoForm from './ContatoForm';
import ExperienciaProfissionalForm from './ExperienciaProfissionalForm';
import FormacaoAcademicaForm from './FormacaoAcademicaForm';

const FormularioCurriculo = () => {
    // Estados para armazenar dados de cada seção
    const [dadosPessoais, setDadosPessoais] = useState({ nome: '', data_nascimento: '' });
    const [contato, setContato] = useState({ email: '', telefone: '', endereco: '' });
    const [experienciaProfissional, setExperienciaProfissional] = useState([]);
    const [formacaoAcademica, setFormacaoAcademica] = useState([]);

    // Funções de atualização de estado para cada formulário
    const handleDadosPessoaisChange = (novoDado) => setDadosPessoais(novoDado);
    const handleContatoChange = (novoContato) => setContato(novoContato);
    const handleExperienciaProfissionalChange = (novaExperiencia) => setExperienciaProfissional(novaExperiencia);
    const handleFormacaoAcademicaChange = (novaFormacao) => setFormacaoAcademica(novaFormacao);

    // Função para lidar com o envio do formulário completo
    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            // Envia cada seção do formulário separadamente ou organiza em uma única requisição se a API permitir
            await api.post('/dadospessoais/', dadosPessoais);
            await api.post('/contato/', contato);
            await api.post('/experienciaprofissional/', { experiencia: experienciaProfissional });
            await api.post('/formacaoacademica/', { formacao: formacaoAcademica });

            alert('Currículo enviado com sucesso!');
        } catch (error) {
            console.error("Erro ao enviar currículo", error);
            alert('Ocorreu um erro ao enviar o currículo.');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Dados Pessoais</h2>
            <DadosPessoaisForm dadosPessoais={dadosPessoais} onChange={handleDadosPessoaisChange} />
            
            <h2>Contato</h2>
            <ContatoForm contato={contato} onChange={handleContatoChange} />
            
            <h2>Experiência Profissional</h2>
            <ExperienciaProfissionalForm experienciaProfissional={experienciaProfissional} onChange={handleExperienciaProfissionalChange} />
            
            <h2>Formação Acadêmica</h2>
            <FormacaoAcademicaForm formacaoAcademica={formacaoAcademica} onChange={handleFormacaoAcademicaChange} />
            
            <button type="submit">Enviar Currículo</button>
        </form>
    );
};

export default FormularioCurriculo;
