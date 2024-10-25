import React, { useState } from 'react';
import api from '../api';

const FormacaoAcademicaForm = () => {
    const [instituicao, setInstituicao] = useState('');
    const [curso, setCurso] = useState('');
    const [inicio, setInicio] = useState('');
    const [fim, setFim] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const dados = { instituicao, curso, inicio, fim };
        try {
            await api.post('/formacaoacademica/', dados);
            alert('Formação acadêmica salva com sucesso!');
        } catch (error) {
            console.error("Erro ao salvar Formação acadêmica", error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Instituição:
                <input type="text" value={instituicao} onChange={(e) => setInstituicao(e.target.value)} />
            </label>
            <label>
                Curso:
                <input type="date" value={curso} onChange={(e) => setCurso(e.target.value)} />
            </label>
            <label>
                Data de ingresso:
                <input type="date" value={inicio} onChange={(e) => setInicio(e.target.value)} />
            </label>
            <label>
                Data de conclusão:
                <input type="date" value={fim} onChange={(e) => setFim(e.target.value)} />
            </label>
            <button type="submit">Enviar</button>
        </form>
    );
};

export default FormacaoAcademicaForm;
